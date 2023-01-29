from bs4 import BeautifulSoup
import requests

def scrape(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    time = soup.find("time")
    title = soup.find("title")
    ret = ""
    for p in soup.find_all("p"):
        ret = ret + p.text
    return "", title.text, ret