from duckduckgo_search import DDGS
import csv
import os

# รายการหัวข้อที่ต้องการค้นหา
topics = [
    "construction materials",
    "Construction products",
    "3D printed houses",
    "Building supplies",
    "Building materials"
]

# สร้างอินสแตนซ์ของ DDGS
with DDGS() as ddgs:
    for topic in topics:
        # ค้นหาข่าวที่เกี่ยวข้องกับหัวข้อ
        results = ddgs.news(topic, max_results=10)

        # ตรวจสอบว่ามีผลลัพธ์หรือไม่
        if results:
            # สร้างชื่อไฟล์ CSV โดยแทนที่ช่องว่างด้วยขีดล่าง
            filename = f"{topic.replace(' ', '_')}_news.csv"

            # เปิดไฟล์ CSV เพื่อเขียนข้อมูล
            with open(filename, mode="w", encoding="utf-8", newline="") as csvfile:
                # กำหนดหัวข้อคอลัมน์จากคีย์ของดิกชันนารีแรก
                fieldnames = results[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # เขียนหัวข้อคอลัมน์
                writer.writeheader()

                # เขียนข้อมูลแต่ละแถว
                writer.writerows(results)

            print(f"บันทึกข่าวสำหรับหัวข้อ '{topic}' สำเร็จลงในไฟล์ {filename}")
        else:
            print(f"ไม่พบผลลัพธ์สำหรับหัวข้อ '{topic}'")
