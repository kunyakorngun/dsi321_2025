import feedparser
import csv
from datetime import datetime

# รายการคำค้นหาที่ต้องการ
keywords = [
    "construction materials",
    "cement industry",
    "Construction supplies",
    "green building",
    "building materials",
    "Sustainable building materials",
    "Eco-friendly building materials",
    "Alternative construction materials"
]

# เวลาที่ดึงข้อมูล
fetch_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# เปิดไฟล์ CSV เพื่อเขียนข้อมูล
with open("scrap_test.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Fetched Time", "Keyword", "Title", "URL"])

    seen_titles = set()

    for keyword in keywords:
        # สร้าง URL สำหรับ RSS Feed
        rss_url = f"https://news.google.com/rss/search?q={keyword.replace(' ', '+')}&hl=en-US&gl=US&ceid=US:en"

        # ดึงข้อมูลจาก RSS Feed
        feed = feedparser.parse(rss_url)

        for entry in feed.entries:
            title = entry.title.strip()
            link = entry.link.strip()

            # ตรวจสอบว่าหัวข้อข่าวซ้ำหรือไม่
            if title not in seen_titles:
                writer.writerow([fetch_time, keyword, title, link])
                seen_titles.add(title)
