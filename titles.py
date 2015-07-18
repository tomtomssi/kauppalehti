__author__ = 'tomtomssi'

import urllib.request
from bs4 import BeautifulSoup
import psycopg2
import config_parser

config = config_parser.ParseConfig()

html = urllib.request.urlopen(config.get_table_url())

soup = BeautifulSoup(html, "html.parser")

table = soup.findAll("table", {"class": "table_stockexchange"})[2]

for header in table.findAll("h3"):
    connection_string = "host='{0}' user='{1}' password='{2}' dbname='{3}'".format(config.get_host(),
                                                                                   config.get_username(),
                                                                                   config.get_password(),
                                                                                   config.get_database())
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO type(name) VALUES ('{0}')".format(header.contents[0]))
    connection.commit()
    connection.close()
