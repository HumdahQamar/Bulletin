import json
import requests

from bs4 import BeautifulSoup
from django.shortcuts import render


ARTICLE_COUNT = 5
API_KEY = 'lNP5pbeh5OIfQa5fsjaZroXmsX4E9JGA'
search_query = 'election'


def get_articles():
    page = requests.get(
        'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=%s&api-key=%s' % (search_query, API_KEY))
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup.find('docs'))
    data = json.loads(str(soup))
    # print(data.get("docs"))
    full_response = data.get('response')
    if full_response:
        docs = full_response.get('docs')
        print(docs)
        if len(docs) > ARTICLE_COUNT:
            docs = docs[:ARTICLE_COUNT]

        news_items = list()
        for doc in docs:
            news_item = dict()
            news_item['headline'] = doc.get('headline').get('main')
            news_item['url'] = doc.get('web_url')
            news_item['abstract'] = doc.get('abstract')
            news_item['lead_paragraph'] = doc.get('lead_paragraph')
            news_items.append(news_items)
        return news_items


def index(request):
    return render(request, 'top_five/index.html')
