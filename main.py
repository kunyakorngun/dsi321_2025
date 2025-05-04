from duckduckgo_search import DDGS
import csv

# สร้างอินสแตนซ์ของ DDGS
with DDGS() as ddgs:
    # ค้นหาข่าวที่เกี่ยวข้องกับ "construction materials"
    results = ddgs.news("construction materials", max_results=10)

# ตรวจสอบว่ามีผลลัพธ์หรือไม่
if results:
    # กำหนดชื่อไฟล์ CSV
    filename = "construction_materials_news.csv"

    # เปิดไฟล์ CSV เพื่อเขียนข้อมูล
    with open(filename, mode="w", encoding="utf-8", newline="") as csvfile:
        # กำหนดหัวข้อคอลัมน์จากคีย์ของดิกชันนารีแรก
        fieldnames = results[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # เขียนหัวข้อคอลัมน์
        writer.writeheader()

        # เขียนข้อมูลแต่ละแถว
        writer.writerows(results)

    print(f"บันทึกข่าวสำเร็จลงในไฟล์ {filename}")
else:
    print("ไม่พบผลลัพธ์สำหรับคำค้นหาที่ระบุ")

