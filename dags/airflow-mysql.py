from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.operators.python import PythonOperator
from airflow.hooks.base import BaseHook
from datetime import datetime

import pandas as pd
import mysql.connector

# DAG definition
dag = DAG(
    'etl_air_quality_to_mysql',
    schedule=None,
    start_date=datetime(2024, 1, 1),
    catchup=False
)

# 1. CREATE TABLE
create_table = SQLExecuteQueryOperator(
    task_id='create_table_mysql',
    conn_id='mysql-local',
    sql="""
    CREATE TABLE IF NOT EXISTS air_quality_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATETIME,
        pm25 DECIMAL(6,3),
        pm10 DECIMAL(6,3),
        no2 DECIMAL(6,3),
        so2 DECIMAL(6,3),
        co DECIMAL(6,3),
        o3 DECIMAL(6,3),
        temperature DECIMAL(5,2),
        humidity DECIMAL(5,2),
        wind_speed DECIMAL(5,3),
        aqi DECIMAL(6,3)
    );
    """,
    dag=dag
)

# 2. EXTRACT & TRANSFORM
def extract_transform(**context):
    import os

    file_path = '/usr/local/airflow/dags/data/air_quality_dataset.csv'
    
    print("FILE EXISTS:", os.path.exists(file_path))

    df = pd.read_csv(file_path)

    print(df.head())

    # Rename columns if needed
    df.columns = [
        'date', 'pm25', 'pm10', 'no2', 'so2',
        'co', 'o3', 'temperature', 'humidity',
        'wind_speed', 'aqi'
    ]

    # Convert date column
    df['date'] = pd.to_datetime(df['date']).astype(str)

    # Handle missing values (basic cleaning)
    df = df.dropna()

    # Optional: ensure numeric types
    numeric_cols = [
        'pm25','pm10','no2','so2','co',
        'o3','temperature','humidity','wind_speed','aqi'
    ]
    df[numeric_cols] = df[numeric_cols].astype(float)

    # Push to XCom
    context['ti'].xcom_push(
        key='air_quality_data', 
        value=df.to_dict('records')
    )

df_task = PythonOperator(
    task_id='extract_transform_task',
    python_callable=extract_transform,
    dag=dag
)

# 3. LOAD
def load_to_mysql(**context):
    records = context['ti'].xcom_pull(
        key='air_quality_data',
        task_ids='extract_transform_task'
    )

    # Get connection from Airflow
    conn = BaseHook.get_connection('mysql-local')
    print("PASSWORD:", conn.password)
    connection = mysql.connector.connect(
        host=conn.host,
        user=conn.login,
        password=conn.password,
        database=conn.schema,
        port=conn.port
    )

    cursor = connection.cursor()

    insert_query = """
    INSERT INTO air_quality_data (
        date, pm25, pm10, no2, so2,
        co, o3, temperature, humidity,
        wind_speed, aqi
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    for row in records:
        cursor.execute(insert_query, (
            row['date'],
            row['pm25'],
            row['pm10'],
            row['no2'],
            row['so2'],
            row['co'],
            row['o3'],
            row['temperature'],
            row['humidity'],
            row['wind_speed'],
            row['aqi']
        ))

    connection.commit()
    cursor.close()
    connection.close()


load_task = PythonOperator(
    task_id='load_to_mysql_task',
    python_callable=load_to_mysql,
    dag=dag
)

# DAG dependencies
create_table >> df_task >> load_task