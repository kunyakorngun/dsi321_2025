import pandas as pd

# โหลดข้อมูลจากไฟล์ CSV
df = pd.read_csv('filtered_by_topic.csv')

# เปลี่ยนชื่อคอลัมน์จาก 'published' เป็น 'timestamp'
df.rename(columns={'published': 'timestamp'}, inplace=True)

# บันทึกข้อมูลเป็นไฟล์ Parquet
df.to_parquet('clean_data.parquet', index=False)
#df.to_parquet('scrap_data.parquet', index=False)

#check_quality
# import pandas as pd

# # อ่านไฟล์ .parquet
# df = pd.read_parquet("output_file.parquet")

# # แสดงข้อมูลบางส่วน
# print(df.head())
