# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup


def _get_phone_model(soup):
    models = list()
    links = soup.find_all('div', class_='p-name p-name-type-2')
    for link in links:
        model = link.find('em').get_text()
        models.append(model)
    return models


def _get_price(soup):
    prices = list()
    links = soup.find('div', id='J_goodsList').find_all('div', class_='p-price')
    for link in links:
        price = float(link.find('strong').find('i').get_text())
        prices.append(price)
    return prices


def _get_evaluation_number(soup):
    numbers = list()
    links = soup.find_all('div', class_='p-commit')
    for link in links:
        number = link.find('strong').find('a').get_text()
        numbers.append(number)
    return numbers


def _get_merchant(soup):
    merchants = list()
    links = soup.find_all('div', class_='p-shop')
    for link in links:
        merchant = link.find('a')
        if not merchant:
            merchants.append('无商家')
        else:
            merchants.append(merchant.get_text())
    return merchants


class Parser(object):
    def parse(self, html):
        print '^ parse'
        soup = BeautifulSoup(html, 'html.parser')
        phone_model = _get_phone_model(soup)
        evaluation_number = _get_evaluation_number(soup)
        merchant = _get_merchant(soup)
        price = _get_price(soup)

        return phone_model, evaluation_number, price, merchant
