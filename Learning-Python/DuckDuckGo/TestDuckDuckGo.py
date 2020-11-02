import bs4 as bs
import urllib.request
import re
import json


def get_search_terms():
    t = []
    word_list = open('Search-Terms.txt', encoding='utf-8')
    for line in word_list:
        word = line.strip()
        t.append(word.lower())
    return t


def get_search_results(search_terms):
    result = dict()
    for term in search_terms:
        term = term.replace(' ', '+')
        term = term.replace('ö', 'o')
        term = term.replace('ä', 'a')
        term = term.replace('ü', 'u')
        url = f'https://html.duckduckgo.com/html?q={term}'
        sauce = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(sauce, 'lxml')
        first_link = soup.findAll(
            'div', {'class': re.compile('links_main*')})[0].a['href']
        first_link = first_link.replace('//duckduckgo.com/l/?uddg=', '')
        first_link = first_link.replace('%3A', ':')
        first_link = first_link.replace('%2F', '/')
        first_link = first_link.replace('%2D', '-')
        result[term] = first_link
    return result


search_terms = get_search_terms()
result_dict = get_search_results(search_terms)
with open("result.json", "w") as outfile:
    json.dump(result_dict, outfile)
