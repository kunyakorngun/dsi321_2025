from prefect import flow, task
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime
import pandas as pd
from time import sleep


@task
def setup_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--lang=en-US")
    service = Service(EdgeChromiumDriverManager().install())
    return webdriver.Edge(service=service, options=options)


@task(cache_policy=None) 
def search_news(driver, keyword, max_pages=2):
    search_url = f"https://www.google.com/search?q={keyword.replace(' ', '+')}&tbm=nws&tbs=sbd:1"
    driver.get(search_url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    titles_links = []
    seen_titles = set()
    page = 1

    while page <= max_pages:
        print(f"📄 กำลังประมวลผลหน้าที่ {page}")
        sleep(2)

        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        sleep(2)

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

        try:
            next_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "pnnext"))
            )
            next_button.click()
            page += 1
        except:
            print("📌 ไม่พบปุ่มถัดไป — จบการดึงข่าว")
            break

    return titles_links


@task
def save_to_csv(data, keyword, filename="Lily of the Valley.csv"):
    df = pd.DataFrame(data, columns=["Title", "Link"])
    df.insert(0, "Fetched Time", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    df.insert(1, "Keyword", keyword)
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"✅ ดึงข่าวได้ทั้งหมด {len(df)} หัวข้อ และบันทึกใน {filename}")


@flow
def news_scraper_flow():
    keyword = "Lily of the Valley"
    driver = setup_driver()
    try:
        results = search_news(driver, keyword)
        save_to_csv(results, keyword)
    finally:
        driver.quit()


if __name__ == "__main__":
    news_scraper_flow()
