import json

with open('result.json') as json_file:
    data = json.load(json_file)

result = open("result.txt", "w")

for key, value in data.items():
    result.write(value)
    result.write("\n")
