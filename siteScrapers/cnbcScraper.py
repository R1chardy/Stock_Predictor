from bs4 import BeautifulSoup
import requests

def scrape(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    results = soup.find(class_=["ArticleBody-articleBody"])
    time = soup.find("time").text
    title = soup.find("title").text
    ret = ""
    for p in results.find_all("p"):
        ret = ret + p.text + "\n"

    return time, title, ret
