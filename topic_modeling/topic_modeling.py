import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import matplotlib.pyplot as plt

# 1. โหลดข้อมูลจาก .parquet
df = pd.read_parquet("../data/data.parquet")

# 2. เลือกเฉพาะคอลัมน์ cleaned_title
texts = df["cleaned_title"].dropna().astype(str).tolist()

# 3. Vectorize ข้อความ (Bag of Words)
vectorizer = CountVectorizer(
    max_df=0.95, 
    min_df=2, 
    stop_words="english"
)
X = vectorizer.fit_transform(texts)

# 4. สร้างและฝึกโมเดล LDA
n_topics = 5  # สามารถปรับได้ตามต้องการ
lda = LatentDirichletAllocation(
    n_components=n_topics, 
    random_state=42
)
lda.fit(X)

# 5. แสดง Top Keywords ของแต่ละ Topic
feature_names = vectorizer.get_feature_names_out()

def print_topics(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print(f"Topic #{topic_idx + 1}:")
        print("  ", " | ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
        print()

print_topics(lda, feature_names, n_top_words=10)

# Optional: แสดงความสำคัญของแต่ละ Topic ในกราฟ
topic_weights = lda.transform(X).sum(axis=0)
plt.bar(range(n_topics), topic_weights)
plt.xlabel("Topic")
plt.ylabel("Weight")
plt.title("Topic Importance")
plt.show()
