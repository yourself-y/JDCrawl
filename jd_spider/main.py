# -*- coding:utf-8 -*-
import time
from selenium.webdriver.common.keys import Keys
from jd_spider import downloader, parser, outputer
from selenium.webdriver.chrome import webdriver


class SpiderMain(object):
    def __init__(self):
        self.downloader = downloader.Downloader()
        self.parser = parser.Parser()
        self.outputer = outputer.Outputer()

    def crawl(self, url):
        print '# begin crawl #'
        browser = webdriver.WebDriver()
        browser.get(url)
        jd_input = browser.find_element_by_id('key')
        jd_input.send_keys('手机'.decode('utf-8'))
        jd_input.send_keys(Keys.ENTER)
        time.sleep(5)
        page = int(browser.find_element_by_class_name('p-skip').find_element_by_css_selector('b').text)
        phone_model = list()
        evaluation_number = list()
        price = list()
        merchant = list()
        i = 0
        while i < page:
            print i
            time.sleep(3)
            html = self.downloader.download(browser)
            phone_model_temp, evaluation_number_temp, price_temp, merchant_temp = self.parser.parse(html)
            phone_model += phone_model_temp
            evaluation_number += evaluation_number_temp
            price += price_temp
            merchant += merchant_temp
            print len(phone_model)
            print len(evaluation_number)
            print len(price)
            print len(merchant)
            next_page = browser.find_element_by_class_name('pn-next')
            next_page.click()
            i += 1
        self.outputer.collect_data(phone_model, evaluation_number, price, merchant)
        browser.close()


if __name__ == '__main__':
    root_url = 'https://search.jd.com/Search'
    spider = SpiderMain()
    spider.crawl(root_url)
    print ('-*- Finish -*-')
