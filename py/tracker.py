
import urllib.request
import urllib.parse
import http.client
from bs4 import BeautifulSoup
import motor.motor_tornado

client = client = motor.motor_tornado.MotorClient('mongodb://localhost:27017')
db = client.raw_webcontent


#url = 'https://arstechnica.com'
#url = 'https://www.amazon.ca/'
#url = 'https://www.wikipedia.org'112
url = 'https://www.hollisterco.com/shop/ca/guys/?filtered=true&rows=240&start=0'
#url='https://www.kijiji.ca/b-house-for-sale/mississauga-peel-region/c35l1700276'

headers = {}
headers['User-Agent'] = "PostmanRuntime/7.20.1"
headers['Accept'] = "*/*"
headers['Cache-Control'] = "no-cache"
headers['Connection'] = "keep-alive"
#headers['Accept-Encoding'] = "gzip, deflate, br"
#headers['Content-Type'] = "text/plain;charset=UTF-8"

# conn = http.client.HTTPSConnection('www.hollisterco.com')
# conn.request("HEAD", "/shop/ca")
# r1 = conn.getresponse()
# print(r1.status, r1.reason)
# data1 = r1.read()
# print(data1)
# conn.close()

#
# conn = http.client.HTTPSConnection('www.hollisterco.com')
# conn.request("GET", "/shop/ca")
# r1 = conn.getresponse()
# print(r1.status, r1.reason)
# data1 = r1.read()
# print(data1)
# conn.close()


try:
   req = urllib.request.Request(url, headers=headers)
   html = urllib.request.urlopen(req).read()
   dsd = html.decode('utf-8')
   #print(dsd)

   soup = BeautifulSoup(dsd, 'html.parser')
   #print(soup.prettify())

   saveFile = open('test.html', 'w')
   saveFile.write(soup.prettify())
   saveFile.close()

   with open("test.html") as fp:
      soup = BeautifulSoup(fp, features="html.parser")
      # print(soup.title)
      # print(soup.title.name)
      # print(soup.title.string)

      # print("Class Name: ", soup.__class__.__name__)
      # object_methods = [method_name for method_name in dir(soup) if callable(getattr(soup, method_name))]
      # print(object_methods)

      #print("All Links")
      #print(soup.find_all('a'))

      #for link in soup.find_all('a'):
      #   print(link.get('href'))

      for pd in soup.find_all('div', class_='product-template', limit=10):
         print("Item Start")
         # print("Class Name: ", pd.__class__.__name__)
         # object_methods = [method_name for method_name in dir(pd) if callable(getattr(pd, method_name))]
         # print(object_methods)

         for header in pd.find_all('div', class_='product-header', limit=1):
            #print(header)
            for badge in header.find_all('div', class_='badge', limit=1):
               print(badge.string)

         for image in pd.find_all('div', class_='product-image-section', limit=1):
            for img in pd.find_all('img', class_='product-card__image', limit=0):
               #print(img['data-src'])
               #print(img['src'])
               print(img.attrs)
               #print(img)

         for pc in pd.find_all('div', class_='product-content', limit=1):
            for pname in pc.find_all('div', class_='product-name', limit=1):
               print(pname.a.string.strip())

            for pdetail in pc.find_all('div', class_='product-detail', limit=1):
               print(pdetail.string.strip())

            for price in pc.find_all('span', class_='product-price-text', attrs={'data-state':'original'}, limit=1):
               print(price.string.strip())
            for price in pc.find_all('span', class_='product-price-text', attrs={'data-state':'discount'}, limit=1):
               print(price.string.strip())
            for price in pc.find_all('span', class_='product-price-text', attrs={'data-state':''}, limit=1):
               print(price.string.strip())

         print("Item End")

      #print(soup.prettify())

except Exception as e:
   print(str(e))



