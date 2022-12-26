from bs4 import BeautifulSoup
import urllib.request
import requests
import math
import time

print('\n')
print('1. Load all positive change rate stocks. \n2. Load all negative change rate stocks. \n3. Load all stocks.')
rate = input('Type \'1\', \'2\' or \'3\' to reply:')
print('\n')
if rate == '1':
    print(f'Loading all positive change rate stocks...')
elif rate == '2':
    print(f'Loading all negative change rate stocks...')
else:
    print(f'Loading all stocks...')

def scrapStock():
    my_url = 'https://finance.yahoo.com/most-active?count=25&offset=0'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    req = urllib.request.Request(url=my_url, headers=headers)
    with urllib.request.urlopen(req) as response:
        page_html = response.read()

    soup = BeautifulSoup(page_html, 'lxml')
    page_info = soup.find('span', class_ = 'Mstart(15px) Fw(500) Fz(s)').span.text
    total = int(page_info.split()[-2])
    page_num = math.ceil(total/25)

    with open("AllStock.txt", "w") as file:
        for idx in range(page_num): 
            url = f"https://finance.yahoo.com/most-active?count=25&offset={idx*25}"
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
            req = urllib.request.Request(url=url, headers=headers)
            html = urllib.request.urlopen(req).read()
            with urllib.request.urlopen(req) as response:
                page_html = response.read()
            soup = BeautifulSoup(page_html, 'lxml')
            stock_table = soup.find('tbody')
            stocks = stock_table.find_all('tr')

            for stock in stocks:
                # print(rate)
                # print(type(rate))
                if rate == '1':
                    # print(stock.find_all('td')[3].text[0])
                    # print(type(stock.find_all('td')[3].text[0]))
                    if stock.find_all('td')[3].text[0] == '+':
                        path = stock.find_all('td')[0].find('a')['href']
                        final_url = f"https://finance.yahoo.com{path}"
                        file.write(f"Company name: {stock.find_all('td')[1].text} \n")
                        file.write(f"Price: {stock.find_all('td')[2].text} \n")
                        file.write(f"Change: {stock.find_all('td')[3].text} \n")
                        file.write(f"%Change: {stock.find_all('td')[4].text} \n")
                        file.write(f"Volume: {stock.find_all('td')[5].text} \n")
                        file.write(f"Avg Vol(3 month): {stock.find_all('td')[6].text} \n")
                        file.write(f"Market Cap: {stock.find_all('td')[7].text} \n")
                        file.write(f"PE Ratio (TTM): {stock.find_all('td')[8].text} \n")
                        file.write(f"Link: {final_url} \n")
                        file.write('\n')
                    else:
                        continue
                elif rate == '2':
                    if stock.find_all('td')[3].text[0] == '-':
                        path = stock.find_all('td')[0].find('a')['href']
                        final_url = f"https://finance.yahoo.com{path}"
                        file.write(f"Company name: {stock.find_all('td')[1].text} \n")
                        file.write(f"Price: {stock.find_all('td')[2].text} \n")
                        file.write(f"Change: {stock.find_all('td')[3].text} \n")
                        file.write(f"%Change: {stock.find_all('td')[4].text} \n")
                        file.write(f"Volume: {stock.find_all('td')[5].text} \n")
                        file.write(f"Avg Vol(3 month): {stock.find_all('td')[6].text} \n")
                        file.write(f"Market Cap: {stock.find_all('td')[7].text} \n")
                        file.write(f"PE Ratio (TTM): {stock.find_all('td')[8].text} \n")
                        file.write(f"Link: {final_url} \n")
                        file.write('\n')
                    else:
                        continue
                else:
                    path = stock.find_all('td')[0].find('a')['href']
                    final_url = f"https://finance.yahoo.com{path}"
                    file.write(f"Company name: {stock.find_all('td')[1].text} \n")
                    file.write(f"Price: {stock.find_all('td')[2].text} \n")
                    file.write(f"Change: {stock.find_all('td')[3].text} \n")
                    file.write(f"%Change: {stock.find_all('td')[4].text} \n")
                    file.write(f"Volume: {stock.find_all('td')[5].text} \n")
                    file.write(f"Avg Vol(3 month): {stock.find_all('td')[6].text} \n")
                    file.write(f"Market Cap: {stock.find_all('td')[7].text} \n")
                    file.write(f"PE Ratio (TTM): {stock.find_all('td')[8].text} \n")
                    file.write(f"Link: {final_url} \n")
                    file.write('\n')

if __name__ == '__main__':
    # while True:
    scrapStock()
    print('\n')
    print(f'All done! Check \'AllStock.txt\'!')
    print('\n')
        # time_wait = 10
        # print(f'Waitng{time_wait} minuters...')
        # time.sleep(time_wait * 60)
