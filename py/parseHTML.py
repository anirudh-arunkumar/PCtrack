from bs4 import BeautifulSoup
from datetime import datetime


class TargetParser:
    def __init__(self, html_path):
        self.file_path = html_path

    def parse(self):
        with open(self.file_path, 'r', encoding='utf8') as f:
            soup = BeautifulSoup(f, features="html.parser")
            #print(soup.prettify())

            data = {
                "date": datetime.utcnow()
            }

            header = soup.find_all(attrs={"data-test": "product-title"})
            if header.__len__()>0:
                #print(header.__getitem__(0).text)
                data["product"] = header.__getitem__(0).text.strip()

            price = soup.find_all(attrs={"data-test": "product-price"})

            if price.__len__()>0:
                data["price"] = price.__getitem__(0).text.strip()
                #print(price)

            print(data)
            return data


