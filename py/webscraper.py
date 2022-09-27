from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time


class WebScraper:
    def __init__(self, geckdrive_path=None):
        self.options = FirefoxOptions()
        self.options.add_argument("--headless")

        self.geckdriver_path = '/Users/saips/base/geckodriver'
        #self.geckdriver_path = 'C:\Anirudh\workspaces\geckodriver-v0.27.0-win64\geckodriver.exe'
        if geckdrive_path is None:
            self.geckdrive_path = geckdrive_path

        self.browser = webdriver.Firefox(options=self.options, executable_path=self.geckdriver_path)

    def get(self, url, outFile):
        self.browser.get(url)
        time.sleep(5)
        with open(outFile, 'w', encoding='utf8') as f:
            f.write(self.browser.page_source)

