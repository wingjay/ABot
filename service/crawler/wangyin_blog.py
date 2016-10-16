import requests

from bs4 import BeautifulSoup


def get_all_blogs():
    base_url = "http://www.yinwang.org/"
    html = requests.get(base_url).text
    soup = BeautifulSoup(html, "html.parser")
    raw_articles = soup.select('.list-group li')
    articles = []
    for a in raw_articles:
        name = a.select('a')[0].get_text()
        url = a.select('a')[0].get('href')
        articles.append({
            'name':  name,
            'url':   url,
        })
    return articles
