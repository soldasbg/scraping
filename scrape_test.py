import requests
from bs4 import BeautifulSoup

url = "https://www.blog.pythonlibrary.org/"

def get_articles():
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")
    pages = soup.findAll('h2')
    articles = {i.a['href']: i.text.strip()
                for i in pages if i.a}
    for article in articles:
        s = '{title}: {url}'.format(
            title=articles[article],
            url=article)
        print(s)
    return articles

print(get_articles())