#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    base_url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "CustomUserAgent"}  # Set a custom User-Agent to avoid Too Many Requests error
    
    url = f"{base_url}{subreddit}/hot.json"
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        
        for i, post in enumerate(posts[:10], start=1):
            title = post["data"]["title"]
            print(f"{i}. {title}")
    else:
        print("None")

