import requests

def get_reddit_posts():

    url = "https://www.reddit.com/r/startups.json?limit=10"

    headers = {
        "User-Agent": "LeadRadarBot/1.0"
    }

    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        print("Request failed:", r.status_code)
        return

    data = r.json()

    for post in data["data"]["children"]:

        title = post["data"]["title"]
        link = "https://reddit.com" + post["data"]["permalink"]

        print(title)
        print(link)
        print("---")


get_reddit_posts()
