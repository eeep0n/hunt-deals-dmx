from threading import Thread
import DMXHelper
import requests
import bs4
from urllib.parse import urljoin
from DMXItem import DMXItem
import time
from datetime import datetime
import codecs
import os

BASE_URL = 'https://www.dienmayxanh.com/'


class DMXHunterThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.target = None
        self.best_item = None
        self.pages = None

    def run(self):
        target = DMXHelper.input_info_target()
        if target.second_parameter == '-nanocell' or target.second_parameter == '-co-thiet-ke-dac-biet':
            url_request = f"https://www.dienmayxanh.com/{target.manufactory}{target.second_parameter}"
        else:
            url_request = f"https://www.dienmayxanh.com/{target.manufactory}?g={target.second_parameter}"
        while True:
            self.__request_parse(url_request)
            time.sleep(3600)

    def __request_parse(self, url_request):
        r = requests.get(url_request)
        if r.ok:
            formatted_html = bs4.BeautifulSoup(r.text, 'lxml')
            list_prices = formatted_html.select('.prdWrFixHe > a > .prdPriceWrapper > .prPrice')
            list_discounts, list_regular_prices, list_names, list_urls, list_final_items = [], [], [], [], []
            for i in list_prices:
                list_names.append(i.parent.parent.attrs['title'])
                list_urls.append(i.parent.parent.attrs['href'])
                list_regular_prices.append(i.find_next_sibling("strong", class_="prOldPrice"))
                list_discounts.append(i.find_next_sibling("span"))
            list_prices[:] = [int(str(list_prices[index].text).replace('₫', '').replace('.', '')) for index, item in enumerate(list_prices)]
            list_discounts[:] = [0 if item is None else item.text for _, item in enumerate(list_discounts)]
            list_regular_prices[:] = [0 if item is None else int(str(item.text).replace('₫', '').replace('.', '')) for _, item in enumerate(list_regular_prices)]
            list_urls[:] = [urljoin(BASE_URL, item) for _, item in enumerate(list_urls)]
            for index, item in enumerate(list_names):
                list_final_items.append(DMXItem(item, list_prices[index], list_urls[index], list_discounts[index], list_regular_prices[index]))
            date = datetime.now().strftime('%d-%m-%Y')
            times = datetime.now().strftime('%H.%M.%S')
            os.mkdir(f'./Data/{date}') if not os.path.isdir(f'./Data/{date}') else None
            file = codecs.open(f'./Data/{date}/{times}.txt', mode='a', encoding='utf-8')
            for item in list_final_items:
                if item.discount != 0:
                    file.write(f'{item.get_info()}\n')
            file.write('\n\n')
            file.close()

