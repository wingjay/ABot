import requests

from bs4 import BeautifulSoup


def get_all_blogs():
    base_url = "https://engineering.pinterest.com/blog"
    html = requests.get(base_url).text
    soup = BeautifulSoup(html, "html.parser")
    raw_articles = soup.select(".views-row")
    articles = []
    for a in raw_articles:
        name = a.select('span .title')[0].string
        url = a.select('.field-content a')[0].get('href')
        time = a.select('.created')[0].string
        preview = {
            'text': a.select('p')[0].get_text()
        }
        articles.append({
            'name':    name,
            'url':     url,
            'time':    time,
            'preview': preview
        })
    return articles
