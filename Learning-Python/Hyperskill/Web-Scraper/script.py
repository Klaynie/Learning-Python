import requests
import json
from bs4 import BeautifulSoup


def clean_raw_jason(raw_json):
    raw_json = str(raw_json)
    json_data = raw_json[raw_json.find('{'): raw_json.rfind('}') + 1]
    return json_data


url = input("Input the URL:\n")
r = requests.get(url)
if r:
    soup = BeautifulSoup(r.content, 'html.parser')
    raw_json = soup.find('script', {"type": "application/ld+json"})
    try:
        json_data = clean_raw_jason(raw_json)
        movie_json = json.loads(json_data)
        movie_data = {}
        movie_data['name'] = movie_json['name']
        movie_data['description'] = movie_json['description']
        print(movie_data)
    except KeyError:
        print("Invalid movie page!")
else:
    print("Invalid movie page!")
