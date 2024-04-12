***💻КУРСОВАЯ РАБОТА 5***

main.py - файл запуска программы.
В рамках проекта происходит получение данных о компаниях и вакансиях с сайта hh.ru по API.
Создается база данных PostgreSQL. Данные заносятся в таблицы "компании" и "вакансии".
Kласс DBManager подключаеся к БД Postgres с использованием библиотеки psycopg2 и используется для выполнения запросов.

Для работы с проектом необходимо.

Клонировать репозиторий на компьютер используя ссылку git@github.com:tatyanaharlamova/coursework_5.git.

Создать зависимости, выполнив команду poetry install.

Создать файл с названием database.ini, который заполняется следующим образом: [postgresql] host=YourHost user=YourUser password=YourPassword port=YourPort

Словарь с данными для подключения к БД мы получаем из функции, находящейся в файле config.py

При запуске файла main.py в терминал ваводится:
*список всех компаний и количество вакансий у каждой компании

*список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию

*среднюю зарплату по вакансиям

*список всех вакансий, у которых зарплата выше средней по всем вакансиям

*список всех вакансий, в названии которых содержится ключевое слово
