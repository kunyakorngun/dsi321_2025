
import csv
import hashlib

# Step 1: Load old hashes
with open('hashed_old.txt', 'r', encoding='utf-8') as f:
    old_hashes = set(line.strip() for line in f)

# Step 2: Load new hashes
with open('hashed_new.txt', 'r', encoding='utf-8') as f:
    new_hashes = set(line.strip() for line in f)

# Step 3: หาค่า hash ที่เหมือนกันทั้งสองไฟล์
common_hashes = old_hashes.intersection(new_hashes)

# เงื่อนไขตรวจสอบว่ามี hash ที่เหมือนกันหรือไม่
if common_hashes:
    with open('news_results.csv', 'r', encoding='utf-8') as infile, \
         open('Realnew_data.csv', 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        matched_count = 0
        for row in reader:
            title = row['Title'].strip()
            date = row['Date'].strip()
            combined = f'{title}{date}'
            hashed = hashlib.sha256(combined.encode('utf-8')).hexdigest()
            
            if hashed in common_hashes:
                writer.writerow(row)
                matched_count += 1

        if matched_count > 0:
            print(f'✅ สร้างไฟล์ Realnew_data.csv จำนวน {matched_count} แถวที่ตรงกันเรียบร้อยแล้ว')
        else:
            print('❗พบ hash ที่ตรงกัน แต่ไม่มีข้อมูลที่ match กันใน news_results.csv')

else:
    print('❌ ไม่มีข้อมูลที่ตรงกัน ไม่สามารถ join กันได้')