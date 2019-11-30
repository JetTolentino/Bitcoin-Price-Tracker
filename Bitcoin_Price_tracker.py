import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

def main () :
    last_price = 0
    while True:
        url = "https://coinmarketcap.com/currencies/bitcoin/"
        headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                  '(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        price = str(soup.findAll('span', {"class": "cmc-details-panel-price__price"}))
        converted_price = price[47:55]
        if converted_price != last_price:
            print("$" + converted_price + " [" + str(datetime.now()) + "]")
        time.sleep(1)
        last_price = converted_price


main()
