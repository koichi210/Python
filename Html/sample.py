import requests
from bs4 import BeautifulSoup

def WebAccess1():
    PROXIES = {
        'http' : 'http://proxy.canon.co.jp:10080',
        'https' : 'http://proxy.canon.co.jp:10080'
    }

    url = "http://www.yomiuri.co.jp/"

    proxy_handler = requests.ProxyHandler(PROXIES)
    opener = request.build_opener(proxy_handler)
    html = opener.open(url).read()

    
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    
    print(response.text)

def WebAccess2():
    proxies = {
        "http" : "http://proxy.canon.co.jp:10080",
        "https" : "http://proxy.canon.co.jp:10080"
    }

    url = "http://www.yomiuri.co.jp/"

    #Proxcy非対応
    #html = urllib2.urlopen("http://example.com")

    #Proxcy対応
    html = requests.get(url, proxies=proxies)
    print(html.text)

    htmlSource = BeautifulSoup(html.content, "html.parser")

    for link in htmlSource.findAll("a"):
        if 'href' in link.attrs:
            print(link.attrs['href'])


if __name__ == "__main__":
    #WebAccess1()
    WebAccess2()
