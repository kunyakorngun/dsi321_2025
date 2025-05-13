import csv
import hashlib


input_file = 'news_results.csv'
output_file = 'hashed_output.txt'

# คำที่ใช้กรอง Date
date_keywords = ['ชั่วโมงที่ผ่านมา', 'วันที่ผ่านมา']

with open(input_file, 'r', encoding='utf-8') as csvfile, open(output_file, 'w', encoding='utf-8') as outfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        title = row['Title']
        date = row['Date']
        
        # ตรวจสอบว่า Date มีคำว่า 'ชั่วโมงที่ผ่านมา' หรือ 'วันที่ผ่านมา'
        if any(keyword in date for keyword in date_keywords):
            # รวม Title และ Date เพื่อสร้าง hash
            combined = f'{title}{date}'
            
            # สร้าง SHA256 hash
            hashed = hashlib.sha256(combined.encode('utf-8')).hexdigest()
            
            # เขียนผลลัพธ์ลงไฟล์
            outfile.write(hashed + '\n')

print(f'บันทึก hash เสร็จสมบูรณ์ในไฟล์: {output_file}')


