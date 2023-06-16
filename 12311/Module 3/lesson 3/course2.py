import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
soup = BeautifulSoup(response.content, features='xml')


Value_of_all_ID = {}
SNV = [] #Simple names Valute
FNV = [] #Full Names Valute
Value_of_ID = []
def GetCourse(course_id):
    dollar = soup.find('Valute', ID=course_id)
    CS_Name = dollar.CharCode.text
    CF_Name = dollar.Name.text
    C_Nominal = dollar.Nominal.text
    C_Value = dollar.Value.text
    SNV.append(CS_Name) #Заполненный Словарь с краткими названиями
    Value_of_ID.append(C_Value)
C_list = soup.find_all('Valute')
for Currency in C_list:
    GetCourse(Currency['ID'])
    FNV.append(Currency['ID'])
for i in range(len(SNV)):
    Value_of_all_ID[SNV[i]] = Value_of_ID[i]

# print(Value_of_all_ID['USD'])


def get_course(Value_Name):
	return  Value_of_all_ID[Value_Name]





