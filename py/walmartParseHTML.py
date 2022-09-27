from bs4 import BeautifulSoup
from datetime import datetime

class WalmartParser:
    def __init__(self, html_path):
        self.file_path = html_path

    def parse(self):
        with open(self.file_path, 'r', encoding='utf8') as f:
            soup = BeautifulSoup(f, features="html.parser")
            #print(soup.prettify())

            data = {
                "date": datetime.utcnow()
            }

            header = soup.find_all(attrs={"class": "prod-ProductTitle prod-productTitle-buyBox font-bold"})
            if header.__len__()>0:
                #print(header.__getitem__(0).text)
                data["product"] = header.__getitem__(0).text.strip()

            price_curr = soup.find_all(attrs={"class": "price-currency"})
            price_char = soup.find_all(attrs={"class": "price-characteristic"})
            price_mant = soup.find_all(attrs={"class": "price-mantissa"})
            price = str(price_curr.__getitem__(0).text.strip()) + str(price_char.__getitem__(0).text.strip())+ '.' + str(price_mant.__getitem__(0).text.strip())

            if price.__len__()>0:
                data["price"] = price
                #print(price)

            print(data)
            return data
