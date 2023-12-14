class AppConfig(object):
    APP_VERSION = "1.0.0"
    # POSTER_URL = "https://image.tmdb.org/t/p/w300/fiVW06jE7z9YnO4trhaMEdclSiC.jpg"
    POSTER_URL = "https://image.tmdb.org/t/p/w300"
    MOVIE_INFO_URL = "https://api.themoviedb.org/3/movie/"

    MOVIE_LINK1 = "https://vidsrc.xyz/embed/movie?imdb="
    MOVIE_LINK2 = "https://vidsrc.to/embed/movie/"
    MOVIE_LINK3 = "https://themoviearchive.site/watch?tmdb="
    MOVIE_LINK4 = "https://vidsrc.xyz/embed/movie?imdb="
    
    TMD_HEADERS_DEFAULT = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYTM1ZTgyMzE4OTc0NTgxNDJmZjljZTE4ODExNWRlNiIsInN1YiI6IjY0OTM0ZDQ1ODliNTYxMDExYzliZDVhMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.AzWnIcxPNgDwGdzeIZ_C3mRC_5_qy-Z-SRPglLjzlNc"
    }

    GITHUB_URL = "https://github.com/upekshaip/movie-downloader"

    INSTRUCTIONS = """Hello there
add all the instructions here"""