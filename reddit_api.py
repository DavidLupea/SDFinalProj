import random
import sqlite3
import json
import time
import os
import requests
import urllib.request

SUBREDDIT_LIST = ["worldnews", "news", "technology", "InternetIsBeautiful", "chemicalreactiongifs", "nostalgia", "todayilearned"]

# RETURN VALUE a list index 0 is title and 1 is link
def get_link():
    random_number = random.randint(0,2)
    output = []
    jsonFile = "https://www.reddit.com/r/{}/hot.json?limit=3"
    jsonFile = jsonFile.format(random.choice(list(SUBREDDIT_LIST)))
    requests.get(jsonFile, headers = {'User-agent': 'your bot 0.1'})
    request = urllib.request.urlopen(jsonFile)
    response = request.read()
    result = json.loads(response)
    link = "http://www.reddit.com" + result["data"]["children"][random_number]["data"]['permalink']
    title = result["data"]["children"][random_number]["data"]["title"]
    output.append(title)
    output.append(link)
    return output
