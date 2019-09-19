#!/usr/bin/python3
# function that queries the Reddit API and returns the number of subscribers
import requests
from sys import argv


def number_of_subscribers(subreddit):
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(argv[1])
        user_agent = "Nildiert"
        headers = {'User-Agent': user_agent}
        response = requests.get(url, headers=headers)
        json_request = response.json()
        data = json_request.get('data')
        number_subscribers = data.get('subscribers')
        return (number_subscribers)
    except Exception as err:
        return (0)
