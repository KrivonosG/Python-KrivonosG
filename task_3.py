import requests
from locale import setlocale, atof, LC_NUMERIC
from bs4 import BeautifulSoup
from datetime import datetime


def currency_rates(currency_code):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'lxml')
    for k in soup.findAll('valute'):
        code = k.find('charcode').text
        if code == currency_code:
            return atof(k.find('value').text), datetime.strptime(soup.valcurs['date'],'%d.%m.%Y').date()

    return None, None


setlocale(LC_NUMERIC, 'French_Canada.1252')
a = input('Введите код валюты: ').upper()
rate, date = currency_rates(a.upper())
