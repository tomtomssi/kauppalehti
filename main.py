__author__ = 'tomtomssi'

import urllib.request
from bs4 import BeautifulSoup

url = "http://www.kauppalehti.fi/5/i/porssi/porssikurssit/lista.jsp?reverse=false&order=alpha&markets=XHEL&volume=cur&psize=50&listIds=kaikki&rdc=14e820ab26f&gics=0&refresh=60&currency=euro#1436701056351"


def getTables():
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    tables = soup.findAll("table", {"class": "table_stockexchange"})[2]

