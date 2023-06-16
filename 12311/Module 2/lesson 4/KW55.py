import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

soup = BeautifulSoup(response.content, features='xml')

# print(soup)


# C_list = soup.find_all('Valute')
# for Currency in C_list:
#     print(Currency['ID'])



def GetCourse(course_id):
    dollar = soup.find('Valute', ID=course_id)
    C_Name = dollar.CharCode.text
    C_Nominal = dollar.Nominal.text
    C_Value = dollar.Value.text
    print(f'( {C_Nominal} шт.) {C_Name} стоит(ят) {C_Value} Рублей.')



C_list = soup.find_all('Valute')
for Currency in C_list:
    GetCourse(Currency['ID'])