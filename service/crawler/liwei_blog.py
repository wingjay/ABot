import requests

from bs4 import BeautifulSoup


def get_all_blogs():
    base_url = "https://engineering.pinterest.com/blog"
    html = requests.get(base_url).text
    soup = BeautifulSoup(html, "html.parser")
    raw_articles = soup.select('article')
    articles = []
    for a in raw_articles:
        name = a.select('.entry-title a')[0].get_text()
        url = a.select('.entry-title a')[0].get('href')
        preview_text = a.select('.entry-content p')[0].string
        if len(preview_text) < 10:
            preview_text += a.select('.entry-content p')[1].string
        articles.append({
            'name':  name,
            'url':   url,
            'preview': {
                'text': preview_text
            }
        })
    return articles
