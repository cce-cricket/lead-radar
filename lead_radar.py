import requests

def get_reddit_posts():
    url = "https://www.reddit.com/r/startups/new.json"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9"
    }

    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        print("Request failed:", r.status_code)
        print(r.text[:300])
        return

    data = r.json()

    for post in data["data"]["children"]:
        title = post["data"]["title"]
        link = "https://reddit.com" + post["data"]["permalink"]

        print(title)
        print(link)
        print("---")

get_reddit_posts()
