import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
soup = BeautifulSoup(response.content, features='xml')
def Dollar_course():
    return soup.find('Valute', ID='R01235').Value.text
