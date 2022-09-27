import urllib.request
import urllib.parse
import time
from bs4 import BeautifulSoup
import motor.motor_tornado


url = 'https://www.walmart.com/ip/Super-Mario-Odyssey-Nintendo-Nintendo-Switch-045496590741/56011600?wmlspartner=wlpa&selectedSellerId=0&&adid=22222222227092961435&wl0=&wl1=g&wl2=c&wl3=207448187187&wl4=pla-336730290171&wl5=9010778&wl6=&wl7=&wl8=&wl9=pla&wl10=8175035&wl11=online&wl12=56011600&veh=sem&gclid=EAIaIQobChMI7baB4Orf7QIVFDeGCh1mGQN-EAQYAyABEgJGFPD_BwE'
browser.get(url)
time.sleep(5)

#browser.save_screenshot("test.png")
with open('walmartTest.html', 'w', encoding='utf8') as f:
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

   saveFile = open('walmartTest.html', 'w')
   saveFile.write(soup.prettify())
   saveFile.close()
except Exception as e:
   print(str(e))

