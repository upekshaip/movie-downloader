import requests
from bin.Process import Process
from bin.Config import AppConfig as AC


class Handle:
    def __init__(self, status):
        self.status = status
        self.process = Process()


    def fix_queary(self, search_txt):
        return str(search_txt).replace(" ", "+")

    def search_movie(self, search_txt):
        query_text = self.fix_queary(search_txt)
        page = 1
        url = f"https://api.themoviedb.org/3/search/movie?query={query_text}&include_adult=false&language=en-US&page={page}"

        res = requests.get(url, headers=AC.TMD_HEADERS_DEFAULT)
        if res.status_code == 200:
            data = res.json()
            current_page = data["page"]
            total_pages = data["total_pages"]
            total_results = data["total_results"]
            results = data["results"]
            print(data)
            
        else:
            self.process.show_warning_popup()
