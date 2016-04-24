#!/usr/bin/python

import urllib2
from MenuParser import MenuParser

MENU_URL = r'http://catedral.prefeitura.unicamp.br/cardapio.php'

def get_menu():
    parser = MenuParser()
    response = urllib2.urlopen(MENU_URL)
    html = response.read()
    parser.feed(html)
    output_data = parser.get_output_data()
    return output_data

def wsgi_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    response_body = get_menu()
    yield response_body

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 80, wsgi_app)
    httpd.serve_forever()
