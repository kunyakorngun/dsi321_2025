import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# โหลด resource ของ nltk (โหลดครั้งเดียวพอ)
nltk.download("punkt")
nltk.download("stopwords")

# โหลด stopwords ภาษาอังกฤษ
stop_words = set(stopwords.words("english"))

# โหลด CSV (ไม่มี header)
df = pd.read_csv("data1.csv", header=None)

# ตั้งชื่อคอลัมน์ใหม่ให้เข้าใจง่าย
df.columns = ["Title"]

# ฟังก์ชันลบ stop words
def remove_stopwords(text):
    if pd.isnull(text):
        return ""
    words = text.split()  # ใช้ split แทน word_tokenize
    filtered = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered)


# ลบ stopwords
df["Title_no_stopwords"] = df["Title"].apply(remove_stopwords)

# บันทึกไฟล์ใหม่
df.to_csv("cleaned_news.csv", index=False, encoding="utf-8-sig")
print("✅ เสร็จแล้ว บันทึกไฟล์เป็น cleaned_news.csv")
