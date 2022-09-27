
import urllib.request
import urllib.parse
import http.client
import time
from bs4 import BeautifulSoup
import motor.motor_tornado
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import codecs

url = 'https://www.target.com/p/super-mario-odyssey-nintendo-switch/-/A-52161284'

options = FirefoxOptions()
options.add_argument("--headless")

browser = webdriver.Firefox(options=options, executable_path='C:\Anirudh\workspaces\geckodriver-v0.27.0-win64\geckodriver.exe')
browser.get(url)
time.sleep(5)

#browser.save_screenshot("test.png")
with open('test.html', 'w', encoding='utf8') as f:
   f.write(browser.page_source)
   #body = browser.find_element_by_xpath("/html/body")
   #f.write(browser.find_element_by_xpath("/html/body"))
browser.quit()

exit(0)

client = client = motor.motor_tornado.MotorClient('mongodb://localhost:27017')
db = client.raw_webcontent

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

      for pd in soup.find_all('div', class_='l-container-fixed', limit=10):
         print("Item Start")
         # print("Class Name: ", pd.__class__.__name__)
         # object_methods = [method_name for method_name in dir(pd) if callable(getattr(pd, method_name))]
         # print(object_methods)

         for header in pd.find_all('h1', class_='Heading__StyledHeading-sc-1m9kw5a-0 crGulm h-margin-b-none h-margin-b-tiny h-text-bold', limit=1):
            #print(header)
            for badge in header.find_all('span', limit=1):
               print(badge.string)

         # for pc in pd.find_all('div', class_='Row-uds8za-0 fMgJXz', limit=1):
         #    for activeslide in pc.find_all('div', class_='slide--active', limit=1):
         #       for dp in activeslide.find_all('div', class_='slideDeckPicture', limit=1):
         #          for img in dp.find_all('img', limit=1):
         #             #print(img['data-src'])
         #             #print(img['src'])
         #             print(img.attrs)
         #             #print(img)

         for pc in pd.find_all('div', class_='style__PriceFontSize-sc-17wlxvr-0 cYCpyy', limit=1):
            print(pc)

         print("Item End")

      #print(soup.prettify())

except Exception as e:
   print(str(e))



