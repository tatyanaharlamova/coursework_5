from src.class_get_vacancies import GetVacanciesFromApi, companies
from src.utils import create_database, save_data_to_database
from src.class_db_manager import DBManager
from config import config

URL = 'https://api.hh.ru/vacancies'


def main():
    params = config()
    vacancies_list = []
    companies_list = []
    vacancies_from_api = GetVacanciesFromApi(URL)
    for company in companies:
        companies_list.append(vacancies_from_api.get_company_dict(company))
        vacancies_list.extend(vacancies_from_api.get_vacancies_list(company))
    create_database('hh_parser', params)
    save_data_to_database(vacancies_list, companies_list, "hh_parser", params)
    db_manager = DBManager('hh_parser')
    print(f'Cписок всех компаний и количество вакансий у каждой компании: '
          f'{db_manager.get_companies_and_vacancies_count()}')
    print(f'Cписок всех вакансий: {db_manager.get_all_vacancies()}')
    print(f'Cредняя зарплата по вакансиям: {db_manager.get_avg_salary()[0][0]} рублей')
    print(f'Cписок всех вакансий, у которых зарплата выше средней: {db_manager.get_vacancies_with_higher_salary()}')
    print(f'Список всех вакансий, в названии которых содержится ключевое слово: '
          f'{db_manager.get_vacancies_with_keyword("менеджер")}')


if __name__ == '__main__':
    main()
