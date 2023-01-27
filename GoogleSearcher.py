from googlesearch import search
from bs4 import BeautifulSoup
import requests
import json

def find(query, nums, domainName):
    links = search(query, tld="com", num=nums, stop=nums, pause=5)
    file = open(domainName + "Links.json", "w")
    jsonString = json.dumps([link for link in links])
    file.write(jsonString)
    file.close()