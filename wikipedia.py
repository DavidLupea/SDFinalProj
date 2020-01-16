import random
import sqlite3
import json
import time
import os
import urllib.request

def get_article():
    jsonFile = "https://en.wikipedia.org/w/api.php?format=json&action=query&generator=random&grnnamespace=0&prop=revisions|images&rvprop=content&grnlimit=1"
    request = urllib.request.urlopen(jsonFile)
    response = request.read()
    result = json.loads(response)
    link = "https://en.wikipedia.org/wiki/"
    title = list(result["query"]["pages"].values())[0]["title"]
    link += title
    return link
