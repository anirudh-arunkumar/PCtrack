from webscraper import WebScraper
from walmartParseHTML import WalmartParser
from Persist import Persist
from AmazonParseHTML import AmazonParser
from gamestopParseHTML import GameStopParser
from bestbuyParseHTML import BestBuyParser
from parseHTML import TargetParser
from WalmartMultiProductParser import WalmartMultiProductParser
from AmazonMultiProductTracker import AmazonMultiProductTracker
from GameStopMultiProductParser import GameStopMultiProductParser
from BestBuyMultiProductParser import BestBuyMultiProductParser


ws = WebScraper(None)
p = Persist('localhost', 27091)
# p = Persist()

# ws.get('https://www.walmart.com/ip/Super-Mario-Odyssey-Nintendo-Nintendo-Switch-045496590741/56011600?wmlspartner=wlpa&selectedSellerId=0&&adid=22222222227092961435&wl0=&wl1=g&wl2=c&wl3=207448187187&wl4=pla-336730290171&wl5=9010778&wl6=&wl7=&wl8=&wl9=pla&wl10=8175035&wl11=online&wl12=56011600&veh=sem&gclid=EAIaIQobChMI7baB4Orf7QIVFDeGCh1mGQN-EAQYAyABEgJGFPD_BwE',
#        'walmartTest.html')
# parser = WalmartParser('walmartTest.html')
# data = parser.parse()
# data['url'] = 'https://www.walmart.com/ip/Super-Mario-Odyssey-Nintendo-Nintendo-Switch-045496590741/56011600?wmlspartner=wlpa&selectedSellerId=0&&adid=22222222227092961435&wl0=&wl1=g&wl2=c&wl3=207448187187&wl4=pla-336730290171&wl5=9010778&wl6=&wl7=&wl8=&wl9=pla&wl10=8175035&wl11=online&wl12=56011600&veh=sem&gclid=EAIaIQobChMI7baB4Orf7QIVFDeGCh1mGQN-EAQYAyABEgJGFPD_BwE'
# p.save_price(data)

# ws.get('https://www.amazon.com/Super-Mario-Odyssey-Nintendo-Switch/dp/B01MUA0D2A/ref=pd_sbs_2?pd_rd_w=CyjL6&pf_rd_p=ed1e2146-ecfe-435e-b3b5-d79fa072fd58&pf_rd_r=Z6YYCDG7P1KYHG87HCVN&pd_rd_r=6b81b01d-fbd7-417a-b5a2-5cc6f18a8a3c&pd_rd_wg=g2AVP&pd_rd_i=B01MUA0D2A&psc=1',
#        'AmazonTest.html')
# parser = AmazonParser('AmazonTest.html')
# data = parser.parse()
# data['url'] = 'https://www.amazon.com/Super-Mario-Odyssey-Nintendo-Switch/dp/B01MUA0D2A/ref=pd_sbs_2?pd_rd_w=CyjL6&pf_rd_p=ed1e2146-ecfe-435e-b3b5-d79fa072fd58&pf_rd_r=Z6YYCDG7P1KYHG87HCVN&pd_rd_r=6b81b01d-fbd7-417a-b5a2-5cc6f18a8a3c&pd_rd_wg=g2AVP&pd_rd_i=B01MUA0D2A&psc=1'
# p.save_price(data)

# ws.get('https://www.bestbuy.com/site/super-mario-odyssey-standard-edition-nintendo-switch/5721722.p?skuId=5721722',
#       'bestbuyTest.html')
# parser = BestBuyParser('bestbuyTest.html')
# data = parser.parse()
# data[
#     'url'] = 'https://www.bestbuy.com/site/super-mario-odyssey-standard-edition-nintendo-switch/5721722.p?skuId=5721722'
# p.save_price(data)

walmart = WalmartMultiProductParser(
    htmlPath='https://www.walmart.com/browse/video-games/playstation-4-ps4-games/2636_1102672_1105671', scrapper=ws)
bestbuy = BestBuyMultiProductParser(
    htmlPath='https://www.bestbuy.com/site/playstation-4-ps4/playstation-4-ps4-video-games/pcmcat296300050018.c?cp=', scrapper=ws)
amazon = AmazonMultiProductTracker(
    htmlPath='https://www.amazon.com/s?i=videogames&bbn=468642&rh=n%3A20972797011&page=', scrapper=ws)
gamestop = GameStopMultiProductParser(
    htmlPath='https://www.gamestop.com/video-games/playstation-4/games?start=', scrapper=ws)
datas = bestbuy.parse()
p.save_products(datas)




# ws.get('https://www.target.com/p/super-mario-odyssey-nintendo-switch/-/A-52161284',
#        'test.html')
# parser = TargetParser('test.html')
# data = parser.parse()
# data['url'] = 'https://www.target.com/p/super-mario-odyssey-nintendo-switch/-/A-52161284'
# p.save_price(data)
#
# ws.get('https://www.gamestop.com/video-games/switch/games/products/super-mario-odyssey/10141908.html', 'gamestopTest.html')
# parser = GameStopParser('gamestopTest.html')
# data = parser.parse()
# data['url'] = 'https://www.gamestop.com/video-games/switch/games/products/super-mario-odyssey/10141908.html'
# p.save_price(data)
