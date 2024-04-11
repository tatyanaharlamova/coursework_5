from src.class_get_vacancies import GetVacanciesFromApi
from src.utils import create_database, save_data_to_database
from src.class_db_manager import DBManager
import psycopg2
from config import config

URL = 'https://api.hh.ru/vacancies'
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


def main():
    params = config()
    # vacancies_list = []
    # companies_list = []
    # vacancies_from_api = GetVacanciesFromApi(URL)
    # for company in companies:
    #     companies_list.append(vacancies_from_api.get_company_dict(company))
    #     vacancies_list.extend(vacancies_from_api.det_vacancies_list(company))
    # create_database('hh_parser', params)
    # save_data_to_database(vacancies_list, companies_list, "hh_parser", params)
    db_manager = DBManager('hh_parser')
    print(db_manager.get_companies_and_vacancies_count())
    print(db_manager.get_all_vacancies())
    print(db_manager.get_avg_salary())
    print(db_manager.get_vacancies_with_higher_salary())
    print(db_manager.get_vacancies_with_keyword("менеджер"))





if __name__ == '__main__':
    main()
