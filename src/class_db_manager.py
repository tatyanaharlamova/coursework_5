import psycopg2
from config import config
params = config()


class DBManager:
    def __init__(self, db_name,):
        self.db_name = db_name

    def execute_(self, query):
        with psycopg2.connect(dbname=self.db_name, **params) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                results = cur.fetchall()
        conn.close()
        return results

    def get_companies_and_vacancies_count(self):
        """
        Метод получает список всех компаний и количество вакансий у каждой компании
        """
        results = self.execute_(
            """
            SELECT company_name, COUNT(*) FROM vacancies
            JOIN companies USING (company_id)
            GROUP BY company_name
            """
            )
        return results

    def get_all_vacancies(self):
        """
        Метод получает список всех вакансий с указанием названия компании, названия вакансии
        и зарплаты и ссылки на вакансию
        """
        results = self.execute_(
            """
            SELECT vacancy_name, company_name, salary, vacancies.url FROM vacancies
            JOIN companies USING (company_id)
            """
            )
        return results

    def get_avg_salary(self):
        """
        Метод получает среднюю зарплату по вакансиям.
        """
        results = self.execute_(
            """
            SELECT AVG(salary) FROM vacancies
            """
            )
        return results

    def get_vacancies_with_higher_salary(self):
        """
        Метод получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        """
        results = self.execute_(
            """
            SELECT * FROM vacancies
            WHERE salary > (SELECT AVG(salary) FROM vacancies)
            """
            )
        return results

    def get_vacancies_with_keyword(self, word):
        """
        Метод получает список всех вакансий, в названии которых содержатся переданные в метод слова
        """
        results = self.execute_(
            f"SELECT * FROM vacancies WHERE vacancy_name LIKE('%{word}%')"
            )
        return results
