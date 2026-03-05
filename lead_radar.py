import requests

def get_hackernews_posts():

    print("Hacker News Posts\n")

    url = "https://hacker-news.firebaseio.com/v0/topstories.json"

    r = requests.get(url)
    story_ids = r.json()[:10]

    for sid in story_ids:

        story = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{sid}.json"
        ).json()

        if story.get("title"):

            print(story["title"])

            if story.get("url"):
                print(story["url"])

            print("---")


def get_producthunt_posts():

    print("\nProduct Hunt Launches\n")

    url = "https://api.producthunt.com/v2/api/graphql"

    print("Product Hunt scraping requires API, skipping for now.")


get_hackernews_posts()
