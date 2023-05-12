from googlesearch import search
import json
from datetime import datetime
import pandas as pd

"""
Parameters:
stocks: an array of strings of stocks
sites: an array of strings of sites to search on, for example "finance.yahoo.com"
start, end: strings of the starting date and ending date of search queries, in the format YYYY-MM-DD

The function uses google to search for every stock on every site in every 5 day range within the entire range. The remainder is also used as a range. It stores 
the links in a json called Searcher2JsonLinks.json. The function still sometimes picks up irrelevant links and also someitmes in different languages. Also gets 
HTTP Error 429: Too Many Requests error occasionally.
"""
def getLinks(stocks, sites, start, end):
    try:
        dates = generateDateArray(start, end)
        pages = set()

        for stock in stocks:
            for site in sites:
                for date1, date2 in zip(dates, dates[1:]):
                    links = googleSearch("site:" + site + " after:" + date1 + " before:" + date2 + " " + stock, 5)
                    for link in links:
                        pages.add(link)
                        print(link)
        
        file = open("Searcher2JsonLinks.json", "w")
        jsonString = json.dumps([link for link in pages])
        file.write(jsonString)
        file.close()
        print("done!")
    except Exception as e:
        print(e)
        file = open("Searcher2JsonLinks.json", "w")
        jsonString = json.dumps([link for link in pages])
        file.write(jsonString)
        file.close()
        print("done!")

def googleSearch(query, nums):
    links = search(query, tld="com", num=nums, stop=nums, pause=5)
    return links
    
def generateDateArray(start, end):
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    date_list = pd.date_range(start_date, end_date, freq='5D')
    if(date_list[-1].strftime("%Y-%m-%d") != end):
        date_list = pd.to_datetime(date_list.tolist() + [end])
    return date_list.strftime("%Y-%m-%d")


def main():
    stocks = ["tesla", "apple", "microsoft", "NVIDIA", "zoom", "blizzard", "google", "iqiyi", "cadence", "qualcomm", "uber"]
    sites = ["news.yahoo.com", "finance.yahoo.com"]
    getLinks(stocks, sites, "2018-01-01", "2018-02-01")

if __name__ == "__main__":
    main()
