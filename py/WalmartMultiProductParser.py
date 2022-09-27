from bs4 import BeautifulSoup
from webscraper import WebScraper
from datetime import datetime
import re
import os


# https://www.walmart.com/browse/video-games/playstation-4-ps4-games/2636_1102672_1105671
class WalmartMultiProductParser:
    def __init__(self, htmlPath, scrapper=None, ):
        if scrapper is None:
            self.scrapper = WebScraper()
        else:
            self.scrapper = scrapper

        self.path = htmlPath

    def parse(self):
        datas = []
        for i in range(1, 2):
            urlPth = self.path + f'?page={i}'
            filepath = f'WalmartMultiProductPage{i}.html'
            self.scrapper.get(urlPth, filepath)

            count = 0
            with open(filepath, 'r', encoding='utf8') as f:
                soup = BeautifulSoup(f, features="html.parser")
                for d in soup.find_all('li', attrs={"data-tl-id": re.compile("ProductTileGridView-*")}):

                    for header in d.find_all('a',
                                             class_='product-title-link line-clamp line-clamp-2 truncate-title'):
                        data = {
                            "date": datetime.utcnow()
                        }
                        data["retailer"] = "Walmart"
                        data["product"] = header.string.strip()
                        print(header.string.strip())
                        
                        images = d.find_all('img')
                        for image in images:
                            print(image['src'])
                            data["image-link"] = image['src']

                        price_char = d.find('span', class_='price-characteristic')
                        pc = price_char
                        price_mant = d.find('span', class_="price-mantissa")
                        pm = price_mant
                        data["price"] = "$" + str(pc.text.strip()) + '.' + str(pm.text.strip())
                        # print("$" + str(pc.text.strip()) + '.' + str(pm.text.strip()))

                        ratings = d.find('span', class_= 'visuallyhidden seo-avg-rating')
                        print(ratings.text.strip())
                        data["rating"] = ratings.text.strip()

                        datas.append(data)
            os.remove(filepath)
        return datas


