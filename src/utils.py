import psycopg2
from config import config
params = config()
companies = {
             'Тинькофф': 78638,
             'WILDBERRIES': 87021,
             'Авито': 84585,
             'Сбер': 3529,
             'Яндекс': 1740,
             'Okko': 1375441,
             'Сбермаркет': 1272486,
             'Skyeng': 1122462,
             'VK': 15478,
             'ГКБ 52': 613491
             }


def create_database(database_name: str, params: dict):
    """Создание базы данных и таблиц для сохранения данных о компаниях и вакансиях"""
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute(f'DROP DATABASE IF EXISTS {database_name}')
        cur.execute(f'CREATE DATABASE {database_name}')
    conn.close()

    conn = psycopg2.connect(dbname='hh_parser', **params)
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute("""
                    CREATE TABLE companies (
                    company_id int PRIMARY KEY,
                    company_name VARCHAR (100) UNIQUE,
                    url varchar(100)
                    )
                    """)
        cur.execute("""
                    CREATE TABLE vacancies (
                    vacancy_id serial PRIMARY KEY,
                    vacancy_name varchar(100) NOT NULL,
                    salary int,
                    area varchar(100),
                    snippet text,
                    url varchar(100),
                    company_id int,
                    CONSTRAINT fk_vacancies_companies FOREIGN KEY(company_id) REFERENCES companies(company_id)
                    )
                    """)

    conn.close()


def save_data_to_database(vacancies_list: list[dict], companies_list,  database_name: str, params: dict):
    """Сохранение данных о компаниях в базу данных."""
    with psycopg2.connect(dbname=database_name, **params) as conn:
        with conn.cursor() as cur:
            for company in companies_list:
                cur.execute(
                    """INSERT INTO companies(company_id, company_name, url)
                    VALUES (%s, %s, %s)""", (company["company_id"], company["company_name"], company["url"])
                )
            for vacancy in vacancies_list:
                cur.execute(
                    """INSERT INTO vacancies(vacancy_name, salary, area, snippet, url, company_id)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    RETURNING vacancy_id""",
                    (vacancy['vacancy_name'], vacancy['salary'], vacancy['area'],
                     vacancy['snippet'], vacancy['url'], vacancy['company_id'])
                )

    conn.close()

