import requests

def get_reddit_posts():
    url = "https://www.reddit.com/r/startups/new.json"
    headers = {"User-Agent": "lead-radar"}

    r = requests.get(url, headers=headers)
    data = r.json()

    for post in data["data"]["children"]:
        title = post["data"]["title"]
        link = "https://reddit.com" + post["data"]["permalink"]

        print(title, link)

get_reddit_posts()
