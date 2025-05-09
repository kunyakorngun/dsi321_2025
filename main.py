from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime
import pandas as pd

# ตั้งค่า WebDriver
options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--lang=en-US")

service = Service(executable_path=r"C:\Users\kunyakorn\Documents\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=options)

# คำค้นหา
keyword = "construction materials"
search_url = f"https://www.google.com/search?q={keyword.replace(' ', '+')}&tbm=nws&tbs=sbd:1"
driver.get(search_url)

# รอหน้าโหลด
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

titles_links = []
seen_titles = set()

page = 1
max_pages = 15

while page <= max_pages:
    print(f"📄 กำลังประมวลผลหน้าที่ {page}")
    sleep(2)
    
    # Scroll หน้า
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    sleep(2)

    # ดึงหัวข้อข่าว
    titles = driver.find_elements(By.CSS_SELECTOR, 'div[role="heading"][aria-level="3"]')

    for title_el in titles:
        try:
            title = title_el.text.strip()
            a_tag = title_el.find_element(By.XPATH, "./ancestor::a")
            link = a_tag.get_attribute("href")
            if title and link and title not in seen_titles:
                titles_links.append((title, link))
                seen_titles.add(title)
        except Exception as e:
            print(f"❌ Error ที่หน้า {page}: {e}")
            continue

    # ลองหาปุ่มถัดไป
    try:
        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "pnnext"))
        )
        next_button.click()
        page += 1
    except:
        print("📌 ไม่พบปุ่มถัดไป — จบการดึงข่าว")
        break

# ปิดเบราว์เซอร์
driver.quit()

# บันทึกลง CSV
df = pd.DataFrame(titles_links, columns=["Title", "Link"])
df.insert(0, "Fetched Time", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
df.insert(1, "Keyword", keyword)

df.to_csv("construction materials.csv", index=False, encoding='utf-8-sig')
print(f"✅ ดึงข่าวได้ทั้งหมด {len(df)} หัวข้อ และบันทึกใน csv")
