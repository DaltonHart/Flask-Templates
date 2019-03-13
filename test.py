import json

with open('subs.json') as json_data:
    d = json.load(json_data)
    for sub in d:
        print(sub['name'])
