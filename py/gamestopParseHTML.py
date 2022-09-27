from bs4 import BeautifulSoup
from datetime import datetime

class GameStopParser:
    def __init__(self, html_path):
        self.file_path = html_path

    def parse(self):
        with open(self.file_path, 'r', encoding='utf8') as f:
            soup = BeautifulSoup(f, features="html.parser")
            #print(soup.prettify())

            data = {
                "date": datetime.utcnow()
            }

            header = soup.find_all(attrs={"class": "product-name h2"})
            if header.__len__()>0:
                #print(header.__getitem__(0).text)
                data["product"] = header.__getitem__(0).text.strip()

            p = soup.find_all(attrs={"class": "primary-details-row"})
            if p.__len__()>0:
                price = p.__getitem__(0)
                price  = price.contents[3].contents[1].contents[1].contents[1].contents[3].contents[1].text
                data["price"] = price.strip()
                #print(price.strip())

            return data