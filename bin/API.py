import requests
from bin.Config import AppConfig as AC


class Handle:
    def __init__(self, status):
        self.status = status

    def fix_queary(self, search_txt):
        return str(search_txt).replace(" ", "+")

    def search_movie(self, search_txt, page):
        query_text = self.fix_queary(search_txt)
        url = f"https://api.themoviedb.org/3/search/movie?query={query_text}&include_adult=false&language=en-US&page={page}"

        res = requests.get(url, headers=AC.TMD_HEADERS_DEFAULT)
        if res.status_code == 200:
            data = res.json()
            current_page = data["page"]
            total_pages = data["total_pages"]
            total_results = data["total_results"]
            results = data["results"]
            return data
            
        else:
            print(f"network error: {res.status_code}")
            return None
