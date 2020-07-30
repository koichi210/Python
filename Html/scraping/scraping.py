#pip install beautifulsoup

#coding: UTF-8
import urllib
from urllib import request
from bs4 import BeautifulSoup

def scraping():
    #url
    url = "http://www.yomiuri.co.jp/"

    #get html
    html = request.urlopen(url)

    #set BueatifulSoup
    soup = BeautifulSoup(html, "html.parser")

    #get headlines
    mainNewsIndex = soup.find("ul", attrs={"class", "list-main-news"})
    headlines = mainNewsIndex.find_all("span", attrs={"class", "headline"})

    #print headlines
    for headline in headlines:
        print(headline.contents[0], headline.span.string)

def scraping_proxy1():
    #url
    url = "http://www.yomiuri.co.jp/"

    PROXIES = {
        'http' : 'http://proxy.canon.co.jp:10080',
        'https' : 'https://proxy.canon.co.jp:10080'
    }

    #urllib.urlopen(url, proxies={"http" : "http://127.0.0.1:8080"})

    proxy_handler = request.ProxyHandler(PROXIES)
    opener = request.build_opener(proxy_handler)
    html = opener.open(url).read()

    soup = BeautifulSoup(html, "html.parser")

    #get headlines
    mainNewsIndex = soup.find("ul", attrs={"class", "list-main-news"})
    headlines = mainNewsIndex.find_all("span", attrs={"class", "headline"})

    #print headlines
    for headline in headlines:
        print(headline.contents[0], headline.span.string)

def scraping_proxy2():
    #url
    url = "http://www.yomiuri.co.jp/"

    PROXIES = {
        'http' : 'http://proxy.canon.co.jp:10080',
        'https' : 'https://proxy.canon.co.jp:10080'
    }

    #html = urllib.urlopen(url, proxies={"http" : "http://127.0.0.1:8080"})
    #html = urllib.urlopen(url, proxies={"http" : "http://proxy.canon.co.jp:10080"})
    #html = urllib.urlopen(url, PROXIES)
    #html = request.urlopen(url, PROXIES)

    soup = BeautifulSoup(html, "html.parser")

if __name__ == "__main__":
    #scraping()
    scraping_proxy1()
    #scraping_proxy2()
