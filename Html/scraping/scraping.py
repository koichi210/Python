#pip install beautifulsoup

#coding: UTF-8
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

if __name__ == "__main__":
    scraping()
