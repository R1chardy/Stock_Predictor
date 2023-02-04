import requests
import siteScrapers.YahooNewsScraper as YahooNewsScraper
from bs4 import BeautifulSoup

def crawl(url):
    try:
        response = requests.get(url)
        time, data = YahooNewsScraper.scrape(url)
        if(len(data.strip()) == 0):
            return []
        print(url)
        print(data)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a')]
        return links
    except:
        return []
    

def main():
    seed_url = "https://finance.yahoo.com/news/look-intrinsic-value-apple-inc-140011914.html"
    pages_to_visit = [seed_url]
    visited_pages = set()
    while pages_to_visit:
        current_page = pages_to_visit.pop(0)
        if current_page in visited_pages:
            continue
        visited_pages.add(current_page)
        links = crawl(current_page)
        pages_to_visit.extend(links)

if __name__ == "__main__":
    main()
