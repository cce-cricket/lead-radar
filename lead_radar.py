import requests
from bs4 import BeautifulSoup

def get_indiehackers_posts():

    print("\nIndie Hackers Posts\n")

    url = "https://www.indiehackers.com/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    posts = soup.find_all("a", class_="feed-item__title-link")

    for post in posts[:10]:

        title = post.text.strip()
        link = "https://www.indiehackers.com" + post["href"]

        print(title)
        print(link)
        print("---")
