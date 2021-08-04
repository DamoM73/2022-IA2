import requests
import json

def jprint(obj):
    if obj.status_code == 200:
        data = obj.json()
        for item in data:
            print(item["title"],item["location"],item["startDateTime"])
    else:
        print("error")


data = requests.get("http://www.trumba.com/calendars/brisbane-city-council.json")
jprint(data)