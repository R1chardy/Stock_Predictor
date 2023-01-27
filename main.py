import YahooNewsScraper
import GoogleSearcher
import json

stocks = ["tesla", "apple", "microsoft", "NVIDIA", "zoom", "blizzard", "google", "iqiyi", "cadence", "qualcomm", "uber"]
YahooNewsBase = "site:news.yahoo.com after:2018-01-01 before:2019-01-01 "
#add more base searches and search functions and scrapers for them

def scrapeYahooNews():
    for stock in stocks:
        print("Scraping " + stock)
        GoogleSearcher.find(YahooNewsBase + stock, 10, "yahoo")
        file = open("yahooLinks.json", "r")
        jsonArr = json.load(file)
        for link in jsonArr:
            print(link)
            time, title, data = YahooNewsScraper.scrape(link)
            print(title)
            print(time)
            print(data)
            print()


if __name__ == "__main__":
    scrapeYahooNews()