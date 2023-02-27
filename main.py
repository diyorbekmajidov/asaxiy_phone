from bs4 import BeautifulSoup
import requests
from tinydb import TinyDB

db = TinyDB("product.json", indent = 4)

db.table('apple')

brand = 'apple'
page = 1
url = f'https://asaxiy.uz/uz/product/telefony-i-gadzhety/telefony/smartfony/brand={brand}/page={page}'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('div', class_='product__item d-flex flex-column justify-content-between')


for product in products:
    # a tegdan herf tegini olish
    link = product.find('a').get('href')
    # a tegdan textni olish
    title = product.find('a').text
    print('https://asaxiy.uz/'+link)
    db.table('apple').insert({"link":link})


