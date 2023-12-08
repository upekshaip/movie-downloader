class Config(object):
    # Main URL
    MAIN_URL = f"https://fmoviesz.to"
    # Base URL
    BASE_URL = f"https://fmoviesz.to/home"

    # Search URL
    key, page = "", ""
    SEARCH_URL = f"https://fmoviesz.to/filter?keyword={key}&page={page}"

    # Headers
    HEADERS = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }






    # tmdb
    search = "https://api.themoviedb.org/3/search/movie?query=fast+and&include_adult=false&language=en-US&page=1"
    external_id = "https://api.themoviedb.org/3/movie/889741/external_ids"

    # moviearchive.site
    url = """

https://api.themoviearchive.site/v3/movie/sources/346698?token=0.TPj48-HVvSr4tk8eSmo8oRvpcA7OW1o2Rnc0bTDFe8q5XPA5Zd_T78XRj-AQKs5sIVIoxVOFY6rjOwHeyCg9yrZMLmf51jL4euO2Tdwm7eFNKAN5wVbxUfLQTH2ui3xx9SuQHYpF3oovHoKZM_dUeo5vHw8KANgjM-j1i3mxNOWHs7dTaHb6o0Cd_1OCr34rot93Q6IoXP4SFVYJ3jRZ4Gjb0cuszzcpFGDBiXha9vpiMyBYm6L78TVKC33xV39jK6NaziKDXLNxp3w3ddubxXXDKgNC-FyqWBMrzsYt6vet-N6fzyWgYPpuyMtA5WDPDYPyXwkBgOcWDrtTd1iKk_h7gXwbBcBsZFAgIkJt3hyaACnpkWg-4Q212QIxEQstDe3ANnF93IetJNnOfkqVgUJt-BvCX7_fCfHDUeY_a2IThRy_AMEITIQFF0f1M73r.5YWZ2cQBuxu8YrloaMHOcw.bf9d6e9f303ee2dc15704f6bea96c5ffbfe8e98b18c0815bbd2a9a0036d48f04
"""