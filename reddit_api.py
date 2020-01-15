import random
import sqlite3
import json
import time
import os
import urllib.request

SUBREDDIT_LIST = ["worldnews", "news", "technology", "InternetIsBeautiful"]

def get_link():
    jsonFile = "https://www.reddit.com/r/{}/top.json?limit=5"
    jsonFile = jsonFile.format(random.choice(list(SUBREDDIT_LIST)))
    return
