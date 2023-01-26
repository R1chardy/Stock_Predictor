from googlesearch import search
from bs4 import BeautifulSoup
import requests
import YahooScraper

query = "site:news.yahoo.com tesla"
links = search(query, tld="co.in", num=10, stop=10, pause=2)

for link in links:
    date, title, data = YahooScraper.scrape(link)
    print(link + '\n' + title + '\n' + date + '\n' + data + '\n')