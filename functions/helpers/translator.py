#!usr/bin/env python
#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

def translate(text):
    response = requests.get('http://frengly.com?src=en&dest=pt&text=' + text + '&email=rembot@gmail.com&password=rembotsifit')
    return response.text

def parsetranslation(text):
    soup = BeautifulSoup(text, 'lxml')
    print soup.prettify()
    # print soup.findAll('translation')

if __name__ == '__main__':
    text = translate('hello')
    parsetranslation(text)