#!/usr/bin/python3
# function that queries the Reddit API and returns the number of subscribers
import requests
from sys import argv


def top_ten(subreddit):
    try:
        url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(argv[1])
        user_agent = "Nildiert"
        headers = {'User-Agent': user_agent}
        response = requests.get(url, headers=headers)
        data = response.json().get('data')
        if data is not None:
            children = data.get('children')
            for i in children:
                print(i.get('data').get('title'))
        else:
            print(None)
    except Exception as err:
        print(None)
