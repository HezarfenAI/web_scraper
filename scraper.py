import time
from pkgutil import get_data

import requests
from bs4 import BeautifulSoup
from googlesearch import search

default_config = [
    {
        "url": "milliyet.com.tr",
        "content_class": "news-content",
        "element": "div"
    },
    {
        'url': 'dipnot.tv',
        'content_class': 'dp-content-details',
        'element': 'div'
    },
    {
        "url": "haberturk.com",
        "content_class": "cms-container",
        "element": "div"
    },
    {
        "url": "sabah.com.tr/",
        "content_class": "topDetail",
        "element": "div"
    }
]


def get_data_with_retry(url: str, retries=3):
    for i in range(retries):
        try:
            response = requests.get(url)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Attempt {i + 1} failed: {e}")
            time.sleep(2)  # Wait before retrying
    raise Exception("Failed to fetch data after retries")

class HezarfenScraper:
    def __init__(self, config = default_config):
        self.config = config

    def get_data(self, url):
        for i in self.config:
            if i["url"] in url:
                try:
                    page = get_data_with_retry(url)
                    soup = BeautifulSoup(page.content, "html.parser")
                    result = soup.find(i["element"], class_=i["content_class"])

                    return result.text.strip()
                except:
                    print("Hata Alındı ve Es geçildi: " + url)
                    return ""

    """def search(self, query):
        for j in search(query, tld="com.tr", num=10, stop=20, pause=2, verify_ssl=False, country="TR"):
            print(j)
            print(self.get_data(j))"""
    def search_news(self, query):
        result = search("site:milliyet.com.tr OR site:dipnot.tv OR site:haberturk.com OR site:sabah.com.tr " + query, tld="com.tr", num=10, stop=50, pause=2, country="TR")

        return result
