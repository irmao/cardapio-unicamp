#!/usr/bin/python

import urllib2
from MenuParser import MenuParser

MENU_URL = r'http://catedral.prefeitura.unicamp.br/cardapio.php'

parser = MenuParser()
response = urllib2.urlopen(MENU_URL)
html = response.read()
parser.feed(html)
