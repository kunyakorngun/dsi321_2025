import pandas as pd
from nltk.corpus import stopwords
import nltk

# โหลด stopwords ของ NLTK
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# เพิ่ม custom stopwords
custom_stopwords = {
    # ข่าวและสื่อ
    "news", "update", "latest", "breaking", "read", "watch", "live", "video",
    "media", "outlet", "journal", "articles", "headline", "source", "coverage", "information",
    
    # การรายงาน/ประกาศ
    "say", "says", "said", "report", "reports", "reported",
    "announced", "introduced", "launch", "revealed", "expects",
    "statements", "highlighted", "unveiled", "discussed", "talk", "asks", "request",

    # เวลา
    "today", "week", "now",

    # บริษัท/องค์กร
    "company", "group", "corporation", "organization", "firm", "business",
    "Ltd", "Inc", "Co", "PLC", "association", "partner", "entity", "owner",

    # การเงิน/ตลาด
    "market", "investment", "opportunity", "cost", "revenue",

    # สถานที่
    "U.S.", "China", "Europe", "Asia", "India", "Africa", "Japan", "Korea",
    "Middle East", "North America", "Latin America",
    "province", "city", "region", "district", "country",

    # คำเชื่อม/คำฟังก์ชัน
    "is", "will", "with", "for", "by", "on", "at", "in", "to",
    "and", "or", "that", "as", "during", "through", "along",
    "from", "above", "around", "of", "between", "under", "over",

    # สินค้า/บริการ
    "products", "services", "materials", "solutions", "technologies", "construction", "building",

    # คำเกี่ยวกับการพัฒนา/นวัตกรรม
    "supply", "demand", "development", "design",
    "engineering", "value", "growth", "trend", "innovation", "technology"
}

stop_words.update(custom_stopwords)

# โหลดไฟล์ CSV ที่มีคอลัมน์หัวข้อครบ
df = pd.read_csv("raw_scrape.csv")

# ฟังก์ชันลบ stopwords จาก Title
def remove_stopwords(text):
    if pd.isnull(text):
        return ""
    words = text.split()
    filtered = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered)

# สร้างคอลัมน์ใหม่ "Title" ที่ถูก clean
df["Title"] = df["Title"].apply(remove_stopwords)

# บันทึกไฟล์ใหม่ (คงคอลัมน์ครบ)
df.to_csv("cleaned_data.csv", index=False, encoding="utf-8-sig")

print("✅ เสร็จแล้ว บันทึกไฟล์เป็น cleaned_data.csv")
