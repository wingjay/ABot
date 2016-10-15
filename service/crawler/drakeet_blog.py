import requests

from bs4 import BeautifulSoup


def get_all_blogs():
    base_url = "https://drakeet.me/"
    html = requests.get(base_url).text
    soup = BeautifulSoup(html, "html.parser")
    raw_articles = soup.select("article")
    articles = []
    for a in raw_articles:
        name = a.select('.entry-title a')[0].string
        url = a.select('.entry-title a')[0].get('href')
        preview = {
            'text':  a.select('.entry-content p')[0].get_text(),
            'image': a.select('.entry-content img')[0].get('src') if len(a.select('.entry-content img')) > 0 else None
        }
        articles.append({
            'name': name,
            'url':  url,
            'preview': preview
        })
    return articles
