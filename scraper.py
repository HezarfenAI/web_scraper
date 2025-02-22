import requests
from bs4 import BeautifulSoup

default_config = [
    {
        "url": "www.milliyet.com.tr",
        "content_class": "news-content",
        "element": "div"
    },
    {
        'url': 'dipnot.tv',
        'content_class': 'dp-content-details',
        'element': 'div'
    },
]

# url = "https://www.milliyet.com.tr/gundem/son-dakika-maydonoz-donere-feto-operasyonu-kayyum-atandi-7313663"
test_url = ''
#'https://dipnot.tv/tr-TR/generative-engine-optimizasyonu-yapay-zeka-ile-seoyu-guclendirin'
#'https://dipnot.tv/tr-TR/yapay-zeka-ile-arama-motoru-algoritmalarinin-evrimi'
#"https://www.milliyet.com.tr/skorer/live-son-dakika-besiktastan-muthis-geri-donus-eyupspor-maglup-oldu-7313183"
# url = ""

class HezarfenScraper:
    def __init__(self, config = default_config):
        self.config = config

    def get_news(self, url):
        for i in self.config:
            if i["url"] in url:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "html.parser")
                result = soup.find(i["element"], class_= i["content_class"])

                return result.text.strip()

scraper = HezarfenScraper()

print(scraper.get_news(test_url))
