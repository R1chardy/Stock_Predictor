import datetime
import requests
import csv

def getCSV(ticker, start, end):
    url = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={start}&period2={end}&interval=1d&events=history&includeAdjustedClose=true'
    
    with requests.Session() as s:
        dl = s.get(url, headers={'User-agent': 'Mozilla/5.0'})

        decoded = dl.content.decode('utf-8')

        return decoded[decoded.index('\n') + 1:]


if __name__ == '__main__':
    print(getCSV('AAPL', 1514793600, 1641024000))