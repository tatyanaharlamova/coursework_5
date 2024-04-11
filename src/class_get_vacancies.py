import requests
import json


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


class GetVacanciesFromApi:
    """
    Класс получения вакансий конкретных компаний по API
    """

    def __init__(self, url):
        self.__url = url

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, new_url):
        self.__url = new_url

    @staticmethod
    def get_company_id(company_name, company_dict) -> int:
        """
        Метод получения id компании по её названию
        """
        if company_name in company_dict.keys():
            for k, v in company_dict.items():
                if k == company_name:
                    return companies[k]
        else:
            print("Компания входит в заданный список")

    def get_vacancies(self, company_name) -> list:
        """
        Метод для получениz вакансий по API, возвращает словарь с вакасиями
        """
        employer_id = self.get_company_id(company_name, companies)
        response = requests.get(self.__url, params={'per_page': 100, 'employer_id': employer_id})
        vacancies = json.loads(response.text)["items"]
        return vacancies

    def get_company_dict(self, company_name) -> dict:
        company_dict = {'company_id': self.get_vacancies(company_name)[0]['employer']['id'],
                        'company_name': self.get_vacancies(company_name)[0]['employer']['name'],
                        'url': self.get_vacancies(company_name)[0]['employer']['url']}
        return company_dict

    def det_vacancies_list(self, company_name) -> list:
        vacancies_list = []
        for vacancy in self.get_vacancies(company_name):
            if not vacancy.get("salary"):
                pass
            else:
                salary = vacancy["salary"].get('from')
                vacancies_dict = {'vacancy_name': vacancy.get('name'),
                                  'salary': salary,
                                  'area': vacancy.get('area')['name'],
                                  'snippet': vacancy.get('snippet')['requirement'],
                                  'url': vacancy.get('url'),
                                  'company_id': vacancy['employer']['id']}
                vacancies_list.append(vacancies_dict)
        return vacancies_list
