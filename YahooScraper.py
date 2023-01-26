from bs4 import BeautifulSoup
import requests

def scrape(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    results = soup.find(class_=["caas-body"])
    time = soup.find("time")
    ret = ""
    for p in results.find_all("p"):
        ret = ret + p.text
    return time.text, ret

# if __name__ == "__main__":
#     scrape("https://finance.yahoo.com/news/look-intrinsic-value-apple-inc-140011914.html")