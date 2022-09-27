from bs4 import BeautifulSoup
from datetime import datetime
from webscraper import WebScraper
import os


class BestBuyMultiProductParser:
   def __init__(self, htmlPath, scrapper=None, ):
      if scrapper is None:
         self.scrapper = WebScraper()
      else:
         self.scrapper = scrapper

      self.path = htmlPath

   def parse(self):
      datas = []
      for i in range(1, 3):
         urlPth = self.path + f'{i}&id=pcmcat296300050018'
         filepath = f'bestbuyPage{i}.html'
         #self.scrapper.get(urlPth, filepath)

         with open(filepath, 'r', encoding='utf8') as f:
            soup = BeautifulSoup(f, features="html.parser")
            for d in soup.find_all('li', class_='sku-item'):

               for header in d.find_all('h4', class_='sku-header'):
                  data = {
                     "date": datetime.utcnow()
                  }
                  data["retailer"] = "Best Buy"
                  data["product"] = header.string.strip()
                  print(header.string.strip())

                  images = d.find_all('img')
                  for image in images:
                     print(image['src'])
                     data["image-link"] = image['src']

                  price = d.find('div', class_='priceView-hero-price priceView-customer-price')
                  print(price.contents[1].contents[2].strip())
                  data["price"] = '$' + price.contents[1].contents[2].strip()

                  ratings = d.find('p', class_='sr-only')
                  print(ratings.string.strip())
                  data["rating"] = ratings.string.strip()

                  datas.append(data)
         os.remove(filepath)
      return datas




