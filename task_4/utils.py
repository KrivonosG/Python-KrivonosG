import requests
from locale import setlocale, atof, LC_NUMERIC
from bs4 import BeautifulSoup


def currency_rates(currency_code):
    setlocale(LC_NUMERIC, 'French_Canada.1252')
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'lxml')
    for k in soup.findAll('valute'):
        code = k.find('charcode').text
        if code == currency_code:
            return atof(k.find('value').text)
    return None
