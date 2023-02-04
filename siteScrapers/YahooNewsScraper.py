from bs4 import BeautifulSoup
import requests

def scrape(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    results = soup.find(class_=["caas-body"])
    time = soup.find("time")
    title = soup.find("title")
    ret = ""
    for p in results.find_all("p"):
        ret = ret + p.text
    return time.text, title.text, ret