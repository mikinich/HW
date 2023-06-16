import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
soup = BeautifulSoup(response.content, features='xml')
def get_course(course_id):
    return soup.find('Valute', ID=course_id).Value.text
