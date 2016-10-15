import requests
from datetime import datetime

from bs4 import BeautifulSoup


def get_all_blogs():
    base_url = "http://wingjay.com"
    html = requests.get(base_url + "/archives/").text
    soup = BeautifulSoup(html, "html.parser")
    posts = soup.select(".post")
    blogs = []
    for post in posts:
        name = post.select(".post-title-link span")[0].string
        url = base_url + post.select(".post-title-link")[0].get('href')

        # 2016-03-12T09:30:50+08:00
        raw_time = str(post.select(".post-time")[0].get('datetime'))
        create_datetime = datetime.strptime(str.split(raw_time, '+')[0], '%Y-%m-%dT%H:%M:%S')
        days_gap = (datetime.now() - create_datetime).days

        blogs.append({
            'name': name,
            'url':  url,
            'days_before': days_gap
        })
        print("name %s" % name)
        print("url %s" % url)
        print("%s days before" % days_gap)

    return blogs
