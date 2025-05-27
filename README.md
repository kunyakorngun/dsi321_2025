# Project: Analyzing Construction Material Trends from Online News Using Web Scraping and ML

## Introduction

This project aims to collect, analyze, and model construction-related news with a focus on alternative materials and environmentally friendly (green) materials. It applies a data pipeline and machine learning techniques to discover insights from recent news in the construction materials industry.

Main objectives:
- Collect construction-related news from Google News
- Analyze the data using Word Cloud and Topic Modeling
- Identify current trends and frequently discussed topics

# Quality Check
| | |
| - | :- |
| ครอบคลุมช่วงเวลา 24 ชั่วโมง | [![ครอบคลุมช่วงเวลา 24 ชั่วโมง](https://github.com/kunyakorngun/dsi321_2025/actions/workflows/check_time.yml/badge.svg)](https://github.com/kunyakorngun/dsi321_2025/actions/workflows/check_time.yml)
 |
| ประเภทข้อมูลไม่มี 'object' | [![ประเภทข้อมูลไม่มี 'object'](https://github.com/kunyakorngun/dsi321_2025/actions/workflows/check_datatype.yml/badge.svg)](https://github.com/kunyakorngun/dsi321_2025/actions/workflows/check_datatype.yml)
 |
| ความสมบูรณ์ของข้อมูล 90% | [![ความสมบูรณ์ของข้อมูล 90%](https://github.com/kunyakorngun/dsi321_2025/actions/workflows/check_missing.yml/badge.svg)](https://github.com/kunyakorngun/dsi321_2025/actions/workflows/check_missing.yml)
 |
| จำนวน record อย่างน้อย 1,000 record | [![จำนวน record อย่างน้อย 1,000 record](https://github.com/kunyakorngun/dsi321_2025/actions/workflows/check_row.yml/badge.svg)](https://github.com/kunyakorngun/dsi321_2025/actions/workflows/check_row.yml)
 |
| ไม่มีข้อมูลซ้ำ | [![ไม่มีข้อมูลซ้ำ](https://github.com/kunyakorngun/dsi321_2025/actions/workflows/check_duplicate.yml/badge.svg)](https://github.com/kunyakorngun/dsi321_2025/actions/workflows/check_duplicate.yml)
 |
- dataset (`data/data.parquet`)

## Project Structure
```
DSI321_2025/
├── .github/
│ └── workflows/
│ ├── check_datatype.yml
│ ├── check_duplicate.yml
│ ├── check_missing.yml
│ ├── check_row.yml
│ └── check_time.yml
├── data/
│ ├── data.parquet
│ └── scrap_data.parquet
├── prepare/
│ ├── csv_to_parquet.py
│ ├── filtered_by_topic.csv
│ └── scrap_data.csv
├── test/
│ ├── collect_data_test.py
│ └── test.ipynb
├── topic_modeling/
│ └── topic_modeling.py
├── visualize/
├── .gitconfig
├── .gitignore
├── config_path.py
├── docker-compose.yml
├── Dockerfile.cli
├── main.py
├── main_2.py
├── pyproject.toml
├── README.md
├── remove_stopword.py
└── requirements.txt
```
## Process Overview

### Tasks Completed

- Scraped news from Google News using `feedparser` and scheduled with **Prefect**
- Targeted a total of **1,000 articles**
- Stored scraped news as **Parquet files** in **LakeFS**, a versioned Data Lake
- After reaching 1,000 articles, performed data cleaning:
  - Removed stopwords
  - Normalized text to string
  - Converted time columns to UTC timestamps
- Generated Word Cloud and performed Topic Modeling

### Example Keywords

Example search queries include:
- "construction materials", "building materials", "building supplies"
- "construction market", "construction chemicals"
- "material shortage", "price increase construction"
- "supply chain construction"
- "green building materials", "sustainable construction"

These keywords were partly based on **BT Materials DSI324** module content.

## Visualization of the Data

### Word Cloud

![wordcloud](./wc.png)

- **Description**: This word cloud was created from cleaned news articles to show which words appeared most frequently.
- **Insight**: Words like green, carbon, concrete, brick, building, tariffs, and sustainable alternatives were commonly mentioned.
- **Tools**: Python `wordcloud` library

**Interpretation**:
This Word Cloud suggests that news coverage during the data collection period heavily focused on sustainable construction materials (e.g., green concrete, low carbon bricks) and economic policy topics (e.g., price and tariffs). 

Notably, the frequent appearance of “tariffs” and “price” indicates a potential policy shift such as increased taxes on traditional materials like concrete. This might drive interest in alternative materials and sustainable construction solutions.

**BT Materials DSI324 Relevance**: The insight suggests that BT Materials may need to adapt their strategy by focusing on green construction trends and responding to policy shifts that could impact material costs and business sustainability.

### Topic Modeling

- **Insight**: Clean energy and alternative material topics were most prominent.

## Modeling Approach

- Used **Latent Dirichlet Allocation (LDA)** for topic modeling
- Preprocessed data with tokenization and stopword removal
- Built Bag-of-Words representation
- Used `gensim.models.LdaModel` with 5 topics

### Results and Evaluation

Topic #1:
- Top words: construction, building, sustainable, green, materials, solutions, carbon, energy, innovation, design
- Interpretation: Covers sustainable construction, green materials, and carbon reduction concepts

Topic #2:
- Top words: supply, chain, shortage, material, prices, increase, impact, delay, logistics, demand
- Interpretation: Discusses material shortages, price surges, and supply chain disruptions

These results indicate themes around:
- Business/stock concerns
- Supply chain issues
- Sustainable technologies
- Innovative marketing in the construction sector

This analysis could be used to forecast industry trends or for strategic planning.

**BT Materials DSI324 Relevance**: The company should consider adopting alternative or sustainable materials to minimize the business impact of potential concrete taxation policies.

## Key Learnings

- LDA effectively highlights topic groupings in large corpora
- Even with diverse sources, scraped news can be meaningfully grouped via ML
- Insights match current real-world trends in the construction materials industry

## Conclusion

This project demonstrates an end-to-end data pipeline for collecting and analyzing news. It highlights the rise of green materials and alternative construction trends.

## Challenges

- At times, scraping yielded no new data; Prefect scheduling had to be adjusted
- Some articles had encoding issues requiring manual correction
- Time zone norecmalization was needed for consistent data

## Future Improvements

- Increase the number of collected news articles and extend the data collection timeframe to better capture long-term trends
- Compare topic trends across different countries or provinces to identify localized shifts or global patterns
- Explore the use of more sophisticated topic modeling techniques such as **BERTopic** or **Transformer-based models** to improve clustering quality and insight extraction