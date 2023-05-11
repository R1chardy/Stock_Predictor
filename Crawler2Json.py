import requests
import siteScrapers.YahooNewsScraper as YahooNewsScraper
import json
from bs4 import BeautifulSoup

def crawl(url, depth):
    pages_to_visit = [url]
    visited_pages = set()
    while depth > 0:
        depth -= 1
        for i in range(len(pages_to_visit)):
            current_page = pages_to_visit.pop(0)
            if current_page in visited_pages:
                continue

            print("expanding " + current_page)

            visited_pages.add(current_page)
            links = getLinks(current_page)
            pages_to_visit.extend(links)
    file = open("Crawler2JsonLinks.json", "w")
    jsonString = json.dumps([link for link in visited_pages])
    file.write(jsonString)
    file.close()

def getLinks(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        links = [soup.select('#wafer-trending-bar > ul > li:nth-child({}) a'.format(i))[0]['href'] for i in range(1,6)]
        # print(links)
        return links
    except Exception as e:
        print(e)
        return []
    
def main():
    crawl("https://finance.yahoo.com/news/disney-earnings-second-quarter-2023-may-10-200858196.html", 20)

if __name__ == "__main__":
    main()
