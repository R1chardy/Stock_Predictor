import YahooScraper
import GoogleSearcher
import json

stocks = ["tesla", "apple", "microsoft", "NVIDIA", "zoom", "blizzard", "google", "iqiyi", "cadence", "qualcomm", "uber"]
base = "site:news.yahoo.com after:2018-01-01 before:2019-01-01 "

def scrapeYahoo():
    for stock in stocks:
        print("Scraping " + stock)
        GoogleSearcher.find(base + stock, 10, "yahoo")
        file = open("yahooLinks.json", "r")
        jsonArr = json.load(file)
        for link in jsonArr:
            print(link)
            time, title, data = YahooScraper.scrape(link)
            print(title)
            print(time)
            print(data)
            print()


if __name__ == "__main__":
    scrapeYahoo()