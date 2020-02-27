import json

users = json.load(open('users.json'))
for i in users["users"]:
    print(i)