import requests
from bs4 import BeautifulSoup
import datetime

def get_page_func():
   date = date_format()
   get_page = requests.get(f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={date}")
   get_page = get_page.content
   soup = BeautifulSoup(get_page, 'xml')

   return soup


def date_format():
  today = datetime.datetime.today().date()
  return f"{str(today).split('-')[2]}/{str(today).split('-')[1]}/{str(today).split('-')[0]}"
  


def get_currencies_values():
  curr = {}

  soup = get_page_func()
  name = soup.find_all('Name')
  values = soup.find_all('Value')
  nominals = soup.find_all('Nominal')
  
  for i, currs in enumerate(name):
    curr[currs.text] = []
    curr[currs.text].append(nominals[i].text)
    curr[currs.text].append(values[i].text)
  return curr




    