#!/usr/bin/python3
"""
Module for querying Reddit API to get top 10 hot posts from a subreddit.

This module provides a function to fetch and display the titles of the
first 10 hot posts from a given subreddit. It handles invalid subreddits
and API errors gracefully.
"""

import requests
import sys

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query

    Returns:
        None: If the subreddit is invalid or an error occurs
    """
    # Reddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Set custom User-Agent to avoid rate limiting
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Disable redirect following
    params = {
        'limit': 10
    }
    
    try:
        # Make the request
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check if the subreddit exists
        if response.status_code == 404:
            print(None)
            return
            
        # Check for other errors
        if response.status_code != 200:
            print(None)
            return
            
        # Parse the JSON response
        data = response.json()
        posts = data['data']['children']
        
        # Print the titles of the top 10 posts
        for post in posts:
            print(post['data']['title'])
            
    except Exception as e:
        print(None)
        return

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

