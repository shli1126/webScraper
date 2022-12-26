from bs4 import BeautifulSoup
import urllib.request
import requests
import math

my_url = 'https://finance.yahoo.com/most-active?count=25&offset=0'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
req = urllib.request.Request(url=my_url, headers=headers)
with urllib.request.urlopen(req) as response:
    page_html = response.read()

soup = BeautifulSoup(page_html, 'lxml')
page_info = soup.find('span', class_ = 'Mstart(15px) Fw(500) Fz(s)').span.text
total = int(page_info.split()[-2])

page_num = math.ceil(total/25)
print(page_num)