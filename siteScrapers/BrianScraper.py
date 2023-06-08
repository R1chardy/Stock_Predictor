from bs4 import BeautifulSoup
import requests

def scrape(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    for s in soup:
        lines = s.text.split('\n')
        for line in lines:
            if(len(line.strip()) != 0):
                print(line.strip())

if __name__ == "__main__":
    scrape("https://aacf.berkeley.edu/index.html")