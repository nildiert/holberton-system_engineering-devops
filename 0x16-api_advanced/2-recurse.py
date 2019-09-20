#!/usr/bin/python3
# function that queries the Reddit API and returns the number of subscribers
import requests
from sys import argv


def recurse(subreddit, hot_list=[], after=""):
    try:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            argv[1], after)
        user_agent = "Nildiert"
        headers = {'User-Agent': user_agent}
        response = requests.get(url, headers=headers)
        data = response.json().get('data')
        after = data.get('after')
        if after is not None:
            hot_list.append(after)
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except Exception as err:
        pass
