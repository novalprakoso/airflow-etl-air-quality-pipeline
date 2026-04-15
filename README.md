# 🌍 Air Quality ETL Pipeline + Dashboard

<div align="center">

End-to-End Data Engineering Project (ETL + BI)  
Built with Apache Airflow, MySQL, and Power BI  

</div>

---

## 📌 Overview

This project demonstrates an end-to-end **ETL (Extract, Transform, Load) pipeline** combined with **Business Intelligence (BI) dashboarding**.

The pipeline processes historical **Air Quality data (2018–2025)** from a CSV dataset, transforms it using Pandas, loads it into a MySQL database, and visualizes insights through an interactive Power BI dashboard.

💡 This project simulates a real-world **Data Engineering workflow**:
- Data ingestion (CSV)
- Data cleaning & transformation
- Workflow orchestration (Airflow)
- Data storage (MySQL)
- Data visualization (Power BI)

---

## 🛠️ Tech Stack

| Layer              | Tools Used |
|------------------|-----------|
| Orchestration     | Apache Airflow |
| Environment       | Docker + Astro CLI |
| Processing        | Python (Pandas) |
| Storage           | MySQL (XAMPP) |
| Visualization     | Power BI |

---

## ⚙️ ETL Pipeline Flow

### 1. Extract
* Read air quality dataset from CSV file

### 2. Transform
* Clean and standardize data
* Handle missing values
* Convert datetime format
* Ensure compatibility with Airflow XCom

### 3. Load
* Insert processed data into MySQL table

---

## 🔄 Workflow (Airflow DAG)


create_table_mysql
↓
extract_transform_task
↓
load_to_mysql_task


---

## 📊 Power BI Dashboard

This project includes a fully interactive Power BI dashboard for data exploration and insights.

### 🔍 Key Metrics

* Avg AQI: **84.03**
* Max AQI: **125.08**
* Avg PM2.5: **80.26**
* Avg Wind Speed: **4.23**

### 📈 Visualizations

* AQI Category Distribution (Good, Moderate, Unhealthy)
* Air Pollution Trends (PM2.5, PM10, NO2)
* Yearly Comparison Analysis
* Monthly Pollution Patterns
* Worst AQI Days Ranking

### 💡 Key Insights

* 📉 Best Air Quality Year: **2019**
* ⚠️ Worst Air Quality Year: **2020**
* 🔥 Highest AQI recorded: **125+**
* 📅 Worst Day: **14 April 2023**
<img width="967" height="546" alt="image" src="https://github.com/user-attachments/assets/f25da2bf-2d42-478f-a85a-df940660daf0" />

---

## 🧠 Key Challenges & Solutions

### ❗ MySQL Connection from Docker
* **Problem:** Airflow container couldn’t connect to local MySQL  
* **Solution:** Use `host.docker.internal` as host

---

### ❗ XCom Serialization Error
* **Problem:** Pandas `Timestamp` not JSON serializable  
* **Solution:** Convert datetime to string before pushing to XCom

---

### ❗ Airflow DAG Not Detected
* **Problem:** DAG file not appearing in Airflow UI  
* **Solution:** Ensure correct `dags/` mounting inside Docker container

---

### ❗ API Limitation (OpenAQ)
* **Problem:** API requires authentication / deprecated endpoints  
* **Solution:** Use alternative dataset (CSV) for stable pipeline

---

## ▶️ How to Run

### 1. Start Airflow


astro dev start


---

### 2. Access Airflow UI


http://localhost:8080


(or check port via `docker ps`)

---

### 3. Configure MySQL Connection

Go to: **Admin → Connections**

| Field    | Value                    |
|----------|--------------------------|
| Host     | host.docker.internal     |
| Login    | root                     |
| Password | (empty if XAMPP default) |
| Port     | 3306                     |

---

### 4. Trigger DAG

* Open DAG: `etl_air_quality_to_mysql`
* Click **Trigger**

<img width="959" height="409" alt="Tampilan Airflow ETL Success" src="https://github.com/user-attachments/assets/094fd8f6-30a4-4950-9ab9-bec9d90af24a" />

---

## 📊 Output

Data is stored in MySQL table:


airflow_project.air_quality_data

<img width="959" height="410" alt="Tampilan SQL - Data Berhasil Load" src="https://github.com/user-attachments/assets/bc9980ad-6a70-4c18-8ade-49049ac2f72d" />

This data is then connected to **Power BI** for visualization.

---

## 🚀 Future Improvements

* Implement **incremental loading (daily ingestion)**
* Replace CSV with **real-time API pipeline**
* Add **data validation layer (Great Expectations)**
* Store data in **Data Warehouse (BigQuery / Snowflake)**
* Automate dashboard refresh
* Add **data lineage & monitoring**

---

## 👨‍💻 Author

**Noval Prakoso**  
Electrical Engineering Graduate | Aspiring Data Engineer

---

## 💡 Why This Project Matters

This project demonstrates:

* End-to-end **Data Engineering workflow**
* Real-world **ETL pipeline implementation**
* Hands-on experience with **Airflow & Docker**
* Ability to handle **data quality & pipeline issues**
* Integration with **Business Intelligence tools**

---

⭐ If you find this project useful, feel free to give it a star!
