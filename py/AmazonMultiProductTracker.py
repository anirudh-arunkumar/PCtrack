from bs4 import BeautifulSoup
from webscraper import WebScraper
from datetime import datetime
import re
import os


class AmazonMultiProductTracker:
   def __init__(self, htmlPath, scrapper=None, ):
      if scrapper is None:
         self.scrapper = WebScraper()
      else:
         self.scrapper = scrapper

      self.path = htmlPath

   def parse(self):
      datas = []
      for i in range(1, 2):
         urlPth = self.path + f'{i}&qid=1609818741&rd=1&ref=sr_pg_{i}'
         filepath = f'AmazonPage{i}.html'
         self.scrapper.get(urlPth, filepath)

         with open(filepath, 'r', encoding='utf8') as f:
            soup = BeautifulSoup(f, features="html.parser")
            for d in soup.find_all('div', class_='a-section a-spacing-medium'):

               for header in d.find_all('span', class_='a-size-medium a-color-base a-text-normal'):
                  print(header.string.strip())
                  data = {
                     "date": datetime.utcnow()
                  }
                  data["retailer"] = "Amazon"
                  data["product"] = header.string.strip()

                  images = d.find_all('img')
                  for image in images:
                     print(image['src'])
                     data["image-link"] = image['src']

                  price_whole = d.find('span', class_='a-price-whole')
                  price_fraction = d.find('span', class_='a-price-fraction')
                  price = '$' + str(price_whole.text.strip()) + str(price_fraction.text.strip())
                  data["price"] = price
                  print(price)

                  ratings = d.find('span', class_='a-icon a-icon-star-small a-star-small-5 aok-align-bottom')
                  print(ratings.text.strip())
                  data["rating"] = ratings.text.strip()

                  datas.append(data)
         os.remove(filepath)
      return datas



