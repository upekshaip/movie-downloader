import requests
import json


img = "https://image.tmdb.org/t/p/w300/dB6Krk806zeqd0YNp2ngQ9zXteH.jpg"

query = "white+house"
page = 1

url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=en-US&page={page}"

imdb_id = "https://api.themoviedb.org/3/movie/{movie_id}/external_ids"


headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYTM1ZTgyMzE4OTc0NTgxNDJmZjljZTE4ODExNWRlNiIsInN1YiI6IjY0OTM0ZDQ1ODliNTYxMDExYzliZDVhMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.AzWnIcxPNgDwGdzeIZ_C3mRC_5_qy-Z-SRPglLjzlNc"
}

# res = requests.get(url, headers=headers)
# if res.status_code == 200:
#     data = res.json()
#     current_page = data["page"]
#     total_pages = data["total_pages"]
#     total_results = data["total_results"]
#     results = data["results"]
#     for result in results:
#         movie_id = result["id"]
#         imdb_id = f"https://api.themoviedb.org/3/movie/{movie_id}/external_ids"
#         id_req = requests.get(imdb_id, headers=headers)
#         print(id_req.json())
        
    
ress = requests.get("https://movie-web.app/search/movie")
cookies = ress.cookies
new = requests.get("https://movie-web.app/media/tmdb-movie-385687", cookies=cookies, headers=headers)
print(new.text)




# dd = {
#         "adult": false,
#         "backdrop_path": "/2wCrEFQAz1PEWTbN1t8Kr7gvxH4.jpg",
#         "genre_ids": [
#             35,
#             10749
#         ],
#         "id": 269281,
#         "original_language": "it",
#         "original_title": "Anna di Brooklyn",
#         "overview": "A beautiful, wealthy widow leaves New York to find herself a husband in the Italian village in which she was born. After many tries she...chooses the village blacksmith.",
#         "popularity": 4.322,
#         "poster_path": "/sZpGKg8ZU2LdVuPXu3lQvZNqFyE.jpg",
#         "release_date": "1958-04-18",
#         "title": "Fast and Sexy",
#         "video": false,
#         "vote_average": 4.909,
#         "vote_count": 11
#     }