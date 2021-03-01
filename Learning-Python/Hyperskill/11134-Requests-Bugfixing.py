import requests


url = 'https://docs.python.org/3/'
r = requests.get(url)

if r.encoding == 'ISO-8859-1':
    print('Right encoding!')
else:
    print('You should change the encoding.')
