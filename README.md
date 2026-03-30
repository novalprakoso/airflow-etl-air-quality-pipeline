# 🚀 ETL Air Quality Pipeline with Airflow, Docker, and MySQL

## 📌 Overview

This project demonstrates an end-to-end **ETL (Extract, Transform, Load) pipeline** built using Apache Airflow.
The pipeline processes air quality data from a CSV dataset, transforms it using Pandas, and loads it into a MySQL database.

This project reflects real-world Data Engineering practices including:

* Workflow orchestration
* Containerized environment
* Data transformation
* Database integration

---

## 🛠️ Tech Stack

* **Apache Airflow** – Workflow orchestration
* **Docker** – Containerized environment
* **Astro CLI** – Airflow project management
* **MySQL (XAMPP)** – Data storage
* **Python (Pandas)** – Data processing

---

## 📂 Project Structure

```
airflow-etl-air-quality/
│
├── dags/
│   └── airflow_mysql.py        # Main DAG (ETL pipeline)
│
├── data/
│   └── air_quality_dataset.csv # Source dataset
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ⚙️ ETL Pipeline Flow

### 1. Extract

* Read air quality dataset from CSV file

### 2. Transform

* Clean column names
* Convert data types (datetime, numeric)
* Handle serialization for Airflow (XCom compatibility)

### 3. Load

* Insert transformed data into MySQL database

---

## 🔄 Workflow (DAG)

```
create_table_mysql
        ↓
extract_transform_task
        ↓
load_to_mysql_task
```

---

## 🧠 Key Challenges & Solutions

### ❗ Issue: MySQL Connection from Docker

* **Problem:** Airflow container couldn’t connect to local MySQL
* **Solution:** Use `host.docker.internal` as host

---

### ❗ Issue: XCom Serialization Error

* **Problem:** Pandas `Timestamp` not JSON serializable
* **Solution:** Convert datetime to string before pushing to XCom

---

### ❗ Issue: MySQL Authentication Error

* **Problem:** Password mismatch in Airflow connection
* **Solution:** Recreate connection with correct credentials

---

## ▶️ How to Run

### 1. Start Airflow

```
astro dev start
```

---

### 2. Access Airflow UI

```
http://localhost:8080
```

(or port shown in Astro CLI -> docker ps)

---

### 3. Configure Connection

* Go to: Admin → Connections
* Add MySQL connection:

  * Host: `host.docker.internal`
  * Login: `root`
  * Password: *(empty if using XAMPP default)*
  * Port: `3306`

---

### 4. Trigger DAG

* Open DAG: `etl_air_quality_to_mysql`
* Click **Trigger**

---

## 📊 Output

* Data successfully stored in MySQL table:

```
airflow_project.air_quality_data
```

---

## 🚀 Future Improvements

* Replace CSV with real-time API ingestion
* Add data validation layer
* Implement scheduling (daily ingestion)
* Integrate with data warehouse (BigQuery / Snowflake)
* Build dashboard visualization (Power BI / Looker Studio)

---

## 👨‍💻 Author

**Noval Prakoso**
Electrical Engineering Graduate | Aspiring Data Engineer

---

## 💡 Why This Project Matters

This project demonstrates:

* Practical understanding of ETL pipelines
* Hands-on experience with Airflow orchestration
* Ability to debug real-world data engineering issues
* Experience working with Docker-based environments

---

⭐ If you find this project useful, feel free to give it a star!
