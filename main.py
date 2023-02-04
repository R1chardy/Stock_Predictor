import siteScrapers.YahooNewsScraper as YahooNewsScraper
import siteScrapers.YahooFinanceScraper as YahooFinanceScraper
import GoogleSearcher
import json
from pathlib import Path
from StockCSV import getCSV

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

def downloadStockData(stock_list):
    for stock in stock_list:
        path = Path(f'./stockHistoricalData/{stock}.csv')
        if not path.is_file():
            fout = open(f'./stockHistoricalData/{stock}.csv', 'w')
            csv_data = getCSV(stock, 1514793600, 1641024000)
            fout.write(csv_data)
            fout.close()


if __name__ == "__main__":
    # scrapeYahooNews()
    downloadStockData(['AAPL', 'TSLA'])