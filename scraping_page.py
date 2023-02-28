# open product.json file
import json
import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB

db = TinyDB("data.json", indent = 4)
db.table('xiaomi')

with open('product.json', 'r') as f:
    data = json.load(f)
    for i in data['xiaomi']:
        url = data['xiaomi'][i]['link']

    # url = data['app']['74']['link']
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        product = soup.find_all('div', class_='more__about-content')
        price = soup.find('span', class_='price-box_new-price').text
        link = soup.find_all('div', class_='swiper-wrapper')[0]
        img_url = link.find_all('img')[0].get('src')

        color = soup.find('h1', class_='product-title').text.split()[-2] 


        brend = soup.find_all('span', class_='text__content-name')[1].text
        model = soup.find_all('span', class_='text__content-name')[0].text
        try:
            memory = soup.find_all('td', class_='text-right')[10].text.strip()
            ram = soup.find_all('td', class_='text-right')[11].text.strip()
            img_url = link.find_all('img')[0].get('src')
            db.table('xiaomi').insert({"price":price, "img_url":img_url, "color":color, "ram":ram.split()[0], "memory":memory.split()[0], "brend":brend, "model":model})
        except:
            print("error")
    # data = soup.find('h1', class_='product-title').text


