import requests
from bs4 import BeautifulSoup
course_date = input('Введите дату в формате dd/mm/yyyy: ')
response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp', params={'date_req' : course_date})

soup = BeautifulSoup(response.content, features='xml')

C_LIST = soup.find_all('Valute')
user_C = input('Введите последовательность букв, с которых начинается название валюты: ').lower()


for currensy in C_LIST:
    C_Name = currensy.Name.text.lower()
    C_Nominal = currensy.Nominal.text
    C_Value = currensy.Value.text
    if C_Name.startswith(user_C):
        print(f'( {C_Nominal} шт.) {C_Name} стоит(ят) {C_Value} Рублей.')