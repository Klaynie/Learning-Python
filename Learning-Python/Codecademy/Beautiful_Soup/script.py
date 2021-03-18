import requests
from bs4 import BeautifulSoup
import pandas as pd

prefix = "https://content.codecademy.com/courses/beautifulsoup/"
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

soup = BeautifulSoup(webpage_response.content, "html.parser")
# print(soup)
# print(soup.p.string)

# for child in soup.div.children:
#     print(child)

turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them:
for a in turtle_links:
  links.append(prefix+a["href"])
    
#Define turtle_data:
turtle_data = {}
#follow each link:
for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  turtle_name = turtle.select(".name")[0].get_text()
  turtle_info = turtle.find("ul").get_text('|').split("|")
  turtle_data[turtle_name] = [turtle_info]

for key, value in turtle_data.items():
    for data in value:
        temp_data = []
        new_data = []
        columns = []
        for item in data:
            if item != '\n':
                temp_data.append(item)
        for item in temp_data:
            split_item = item.split(': ')
            columns.append(split_item[0])
            new_data.append(split_item[1])
        turtle_data[key] = new_data

turtle_df = pd.DataFrame.from_dict(turtle_data, orient='index', columns=columns)

print(turtle_df)