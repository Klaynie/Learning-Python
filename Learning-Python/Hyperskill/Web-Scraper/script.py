import requests

url = input("Input the URL:\n")
r = requests.get(url)
if r:
    json_data = r.json()
    try:
        print(json_data['content'])
    except KeyError:
        print("Invalid quote resource!")
else:
    print("Invalid quote resource!")
