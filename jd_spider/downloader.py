# -*- coding:utf-8 -*-
import time

from selenium.webdriver.common.keys import Keys


class Downloader(object):
    def download(self, browser):
        print '^ download'
        body = browser.find_element_by_css_selector('body')
        i = 0
        while i < 16:
            time.sleep(3)
            body.send_keys(Keys.PAGE_DOWN)
            i += 1
        print '滚动结束'

        return browser.page_source
