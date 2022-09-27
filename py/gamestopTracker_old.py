import urllib.request
import urllib.parse
import http.client
import time
from bs4 import BeautifulSoup
import motor.motor_tornado
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import codecs

url = 'https://www.gamestop.com/video-games/switch/games/products/super-mario-odyssey/10141908.html'

options = FirefoxOptions()
options.add_argument("--headless")

browser = webdriver.Firefox(options=options, executable_path='C:\Anirudh\workspaces\geckodriver-v0.27.0-win64\geckodriver.exe')
browser.get(url)
time.sleep(5)

#browser.save_screenshot("test.png")
with open('gamestopTest.html', 'w', encoding='utf8') as f:
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

   saveFile = open('gamestopTest.html', 'w')
   saveFile.write(soup.prettify())
   saveFile.close()
except Exception as e:
   print(str(e))


