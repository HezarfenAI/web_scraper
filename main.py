import csv
import re
import time

import pandas as pd
import numpy as np
import scraper as sc

urls = [

]

art = """

  _    _                     __                      _____    _____                                
 | |  | |                   / _|               /\   |_   _|  / ____|                               
 | |__| | ___ ______ _ _ __| |_ ___ _ __      /  \    | |   | (___   ___ _ __ __ _ _ __   ___ _ __ 
 |  __  |/ _ \_  / _` | '__|  _/ _ \ '_ \    / /\ \   | |    \___ \ / __| '__/ _` | '_ \ / _ \ '__|
 | |  | |  __// / (_| | |  | ||  __/ | | |  / ____ \ _| |_   ____) | (__| | | (_| | |_) |  __/ |   
 |_|  |_|\___/___\__,_|_|  |_| \___|_| |_| /_/    \_\_____| |_____/ \___|_|  \__,_| .__/ \___|_|   
                                                                                  | |              
                                                                                  |_|             
    [1] Manuel Veri Girmek İçin
    [2] Online Veri Çekmek İçin
    [3] Modeli Eğitmek İçin         [Çalışmıyor]
    [4] Modeli Test Etmek İçin      [Çalışmıyor]
    [5] Modeli Kaydetmek İçin       [Çalışmıyor]
    [6] Modeli Yüklemek İçin        [Çalışmıyor]
    [7] Çıkış Yapmak İçin           [Çalışmıyor]
"""

def scrape(query: str):
    scraper = sc.HezarfenScraper()
    news = scraper.search_news(query)
    data = []
    df = pd.read_csv('../hezarfen_ai/datasets/turkish_news.csv')
    urls = df.iloc[:, 2]
    for i in news:
        print(scraper.get_data(i))
        text = scraper.get_data(i)
        if not urls.str.contains(re.escape(i), na=False).any() and text is not None and text.strip() != "":
            data.append({"text": text, "label": "REAL", "url": i})
            print("Data Eklendi ", i)
        else:
            print("Data Zaten Var , i")
        print("--------------------------------------------------")
        time.sleep(1)

    with open('../hezarfen_ai/datasets/turkish_news.csv', 'a', newline='') as csvfile:
        fieldnames = ['text', 'label', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows(data)

    new_df = pd.read_csv('../hezarfen_ai/datasets/turkish_news.csv')
    print("---------------------------------", len(data), "[Data Eklendi] ---------------------------------")
    print("---------------------------------", len(df), "'den ", len(new_df), "Uzunluğa Ulaştı ---------------------------------")

def manuel_save(text, label, url):
    with open('../hezarfen_ai/datasets/turkish_news.csv', 'a', newline='') as csvfile:
        fieldnames = ['text', 'label', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"text": text, "label": "REAL" if label == "1" else "FAKE", "url": url})
        print("|", text, "|", "REAL" if label == "1" else "FAKE", "|", url, "|")
        print("--------------------------------- [Data Eklendi] ---------------------------------")

if __name__ == "__main__":
    print(art)
    choise = input("Seçiminizi Yapınız: ")
    if choise == "1":
        while True:
            text = input("Metni Giriniz: ")
            label = input("Etiketi Giriniz [1: REAL, 0: FAKE]: ")
            url = input("Url'yi Giriniz: ")
            manuel_save(text, label, url)

    elif choise == "2":
        while True:
            prompt = input("Ne Aramak İstersiniz? ")
            scrape(prompt)

