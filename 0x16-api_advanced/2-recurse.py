#!/usr/bin/python3
''' Recursive function '''
import requests


def recurse(subreddit, hot_list=[], after=""):
    ''' Recursive function '''
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit, after)
    user_agent = "Nildiert"
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response:
        data = response.json().get('data')
        children = data.get('children')
        after = data.get('after')
        [hot_list.append(tit.get('data').get('title') for ti in children)]
        if after is not None and children:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
