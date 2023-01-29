import YahooNewsScraper
import YahooFinanceScraper
import GoogleSearcher
import json

stocks = ["tesla", "apple", "microsoft", "NVIDIA", "zoom", "blizzard", "google", "iqiyi", "cadence", "qualcomm", "uber"]

#add more base searches and search functions and scrapers for them
YahooNewsBase = "site:news.yahoo.com after:2018-01-01 before:2019-01-01 "
YahooFinanceBase = "site:finance.yahoo.com after:2018-01-01 before:2019-01-01 "

def scrapeYahooNews():
    for stock in stocks:
        print("Scraping " + stock)
        GoogleSearcher.find(YahooNewsBase + stock, 10, "yahooNews")
        file = open("yahooNewsLinks.json", "r")
        jsonArr = json.load(file)
        for link in jsonArr:
            print(link)
            time, title, data = YahooNewsScraper.scrape(link)
            print(title)
            print(time)
            print(data)
            print()

def scrapeYahooFinance():
    for stock in stocks:
        print("Scraping " + stock)
        GoogleSearcher.find(YahooFinanceBase + stock, 10, "yahooFinance")
        file = open("yahooFinanceLinks.json", "r")
        jsonArr = json.load(file)
        for link in jsonArr:
            print(link)
            time, title, data = YahooFinanceScraper.scrape(link)
            print(title)
            print(time)
            print(data)
            print()


if __name__ == "__main__":
    # scrapeYahooNews()
    scrapeYahooFinance()