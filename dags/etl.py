from airflow import DAG
from airflow.decorators import task
from airflow.hooks.base import BaseHook   

from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime

with DAG(
    dag_id="nasa_apod_postgres",
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    @task
    def create_table():
        postgres_hook = PostgresHook(postgres_conn_id="my_postgres_connection")

        create_table_query = """
        CREATE TABLE IF NOT EXISTS apod_data(
            id SERIAL PRIMARY KEY,
            date DATE,
            title VARCHAR(255),
            explanation TEXT,
            url TEXT,
            media_type VARCHAR(50)
        );
        """
        postgres_hook.run(create_table_query)

    @task
    def extract_apod():
        conn = BaseHook.get_connection("nasa_api")
        api_key = conn.extra_dejson["api_key"]

        http_hook = HttpHook(method="GET", http_conn_id="nasa_api")
        response = http_hook.run(
        endpoint=f"planetary/apod?api_key={api_key}"
    )
        return response.json()

    @task
    def transform_apod_data(response: dict):
        return {
            "date": response["date"],
            "title": response["title"],
            "explanation": response["explanation"],
            "url": response["url"],
            "media_type": response["media_type"],
        }

    @task
    def load_apod_data_to_postgres(apod_data: dict):
        postgres_hook = PostgresHook(postgres_conn_id="my_postgres_connection")

        insert_query = """
        INSERT INTO apod_data (date, title, explanation, url, media_type)
        VALUES (%s, %s, %s, %s, %s);
        """
        postgres_hook.run(
            insert_query,
            parameters=(
                apod_data["date"],
                apod_data["title"],
                apod_data["explanation"],
                apod_data["url"],
                apod_data["media_type"],
            ),
        )

    
    table = create_table()
    apod = extract_apod()
    transformed = transform_apod_data(apod)
    load_apod_data_to_postgres(transformed)

    table >> apod
                   