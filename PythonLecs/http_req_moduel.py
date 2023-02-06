import requests
# r = requests.get('https://www.w3schools.com/')
# print(r.text)
# url="https://www.facebook.com/?stype=lo&jlou=AffZdOYiozWUas0-1PBZ-BXYuf_BKPnM06vbVfXkA38w1zP2OvK5wrydQ_VDqlInxrgmVx7wxkZjCtNp7WjYqOWt__jZkCtL7FZaypA7YIC94A&smuh=39050&lh=Ac-anJQ9DrW0XSwVq6c"
# data={"username":"03124414587","password":"noclass"}
# r2=requests.post(url=url,data=data)
# print(r2.status_code)
# if r2 == "200":
#     print("Ok")
# else:
#     print("Not ok")



# Json module

import json

data = '{"var1":"harry", "var2":56}'
print(data)

parsed = json.loads(data)
print(type(parsed))

#Task 1 - json.load?


data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)

# Task 2 = what is sort_keys parameter in dumps










