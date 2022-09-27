from bs4 import BeautifulSoup
from webscraper import WebScraper
from datetime import datetime
import os

scrapper = WebScraper()


class GameStopMultiProductParser:
   def __init__(self, htmlPath, scrapper=None, ):
      if scrapper is None:
         self.scrapper = WebScraper()
      else:
         self.scrapper = scrapper

      self.path = htmlPath

   def parse(self):
      datas = []
      for i in range(0, 24, 12):
         urlPth = self.path + f'{i}&sz=12'
         i = int(i/12) + 1
         filepath = f'gamestopPage{i}.html'

         #TODO
         #Delte the HTML file after parsing
         self.scrapper.get(urlPth, filepath)
         print("Finished fetching "+filepath)
         with open(filepath, 'r', encoding='utf8') as f:
            soup = BeautifulSoup(f, features="html.parser")

            for d in soup.find_all('div', class_='product grid-tile'):
               for header in d.find_all('p', class_='pd-name'):
                  data = {
                     "date": datetime.utcnow()
                  }
                  data["retailer"] = "Gamestop"
                  data["product"] = header.string.strip()
                  print(header.string.strip())

                  #TODO
                  #remove this for loop there will only on price here
                  price = d.find_all('span', class_='actual-price')
                  data["price"] = price.string.strip()
                  print(price.string.strip())
                  datas.append(data)
         os.remove(filepath)
      return datas





