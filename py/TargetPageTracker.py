from bs4 import BeautifulSoup
from webscraper import WebScraper
from datetime import datetime



try:
   for i in range(0, 1):
      urlPth = f'https://www.target.com/c/playstation-4-games-video/-/N-55krz?Nao={i}'
      filepath = 'TargetPage1.html'
      #scrapper.get(urlPth, filepath)

      with open(filepath, 'r', encoding='utf8') as f:
         soup = BeautifulSoup(f, features="html.parser")
         data = {
            "date": datetime.utcnow()
         }

      for d in soup.find_all('li', class_='Col-favj32-0 bTvKos h-padding-a-none h-display-flex'):
         for header in d.find_all('a', class_='Link-sc-1khjl8b-0 styles__StyledTitleLink-mkgs8k-5 dJwaza jqiYMz h-display-block h-text-bold h-text-bs flex-grow-one'):
            print(header.string.strip())
            for price in d.find_all('span', class_='h-text-bs'):
               print(price.string.strip())


except Exception as e:
   print(str(e))


