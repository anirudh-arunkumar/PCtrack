from bs4 import BeautifulSoup
from datetime import datetime
from webscraper import WebScraper


scrapper = WebScraper()
try:
   for i in range(1, 28):
      urlPth = f'https://www.bestbuy.com/site/playstation-4-ps4/playstation-4-ps4-video-games/pcmcat296300050018.c?cp={i}&id=pcmcat296300050018'
      filepath = f'bestbuyPage{i}.html'
      scrapper.get(urlPth, filepath)

      with open(filepath, 'r', encoding='utf8') as f:
         soup = BeautifulSoup(f, features="html.parser")
         data = {
            "date": datetime.utcnow()
         }
         for d in soup.find_all('li', class_='sku-item'):

            for header in d.find_all('h4', class_='sku-header'):
               data["retailer"] = "Best Buy"
               data["product"] = header.string.strip()
               #print(header.string.strip())
               for price in d.find_all('div', class_='priceView-hero-price priceView-customer-price'):
                  #print(price.contents[1].contents[2].strip())
                  data["price"] = '$' + price.contents[1].contents[2].strip()


except Exception as e:
   print(str(e))



