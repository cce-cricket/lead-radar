import requests

KEYWORDS = [
    "startup",
    "saas",
    "launch",
    "founder",
    "mvp",
    "product",
    "growth",
    "customers",
    "build",
]

def get_hackernews_posts():

    print("Startup-related Hacker News Posts\n")

    url = "https://hacker-news.firebaseio.com/v0/newstories.json"

    r = requests.get(url)
    story_ids = r.json()[:30]

    for sid in story_ids:

        story = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{sid}.json"
        ).json()

        title = story.get("title", "").lower()

        if any(k in title for k in KEYWORDS):

            print(story["title"])

            if story.get("url"):
                print(story["url"])

            print("---")


get_hackernews_posts()
