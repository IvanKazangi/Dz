import requests
from bs4 import BeautifulSoup
import lxml

url = "https://rozetka.com.ua/notebooks/c80004/"
user = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

response = requests.get(url, headers=user)
print(response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    # print(soup)

    all_product = soup.find("ul", class_="catalog-grid ng-star-inserted")
    # print(all_product)
    product = all_product.find_all("li", class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
    for prod in product:
        print(prod.text)
    for prod in product:
        old_price = prod.find("div", class_="goods-tile__price--old price--gray ng-star-inserted")
        if old_price.text != "":
            print(old_price.text)
