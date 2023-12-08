import requests
from bs4 import BeautifulSoup
from Config import Config

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Search:
    def __init__(self, status):
        self.status = status

    def write(self, file, data):
        with open(file, "w") as f:
            f.write(data)

    def send_req(self, url):
        f_res = requests.get(Config.BASE_URL, headers=Config.HEADERS)
        res = requests.get(url,headers=Config.HEADERS, cookies=f_res.cookies)
        if res.status_code == 200:
            return res
        else:
            return None


    def search(self, key, page):
        SEARCH_URL = f"https://fmoviesz.to/filter?keyword={key}&page={page}"
        
        res = self.send_req(SEARCH_URL)
        
        if res:
            soup = BeautifulSoup(res.text, "html.parser")

            item_divs = soup.select("div.item")

            final = []
            for item in item_divs:
                dic = {}

                dic["quality"] = item.select_one("div.quality").text
                poster = item.select_one("div.poster")
                dic["movie_page"] = poster.select_one("a").get("href")
                dic["poster"] = poster.select_one("a").select_one("img.lazyload").get("data-src")
                meta = item.select_one("div.meta")
                spans = meta.select("span")
                dic["year"] = spans[0].text
                dic["type"] = meta.select_one("span.type").text
                dic["name"] = meta.select_one("a").text
                dic["duration"] = spans[-1].text
                
                final.append(dic)
        else:
            final = None

        return final

    def get_movie(self, data):
        res = self.send_req(f"{Config.MAIN_URL}{data['movie_page']}")
        if res:
            print(res.text)
            self.write("movies.html", res.text)
            pass
        else:
            pass

    def test(self):
        url = "https://vidsrc.to/embed/movie/385687"
        driver = webdriver.Chrome()

        # try:
          
        driver.get(url)
        time.sleep(3)
        cookies = driver.get_cookies()
        


        print("Page Title:", driver.title)
        html_source = driver.page_source
        print(html_source)
        input()

        # finally:
        #     driver.quit()




search = Search("ok")
# data = search.search("hello", 1)[0]
# print(data)
search.test()
# search.get_movie(data)