import json
import requests

from bs4 import BeautifulSoup
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Query
from top_five.helpers.article import Article


ARTICLE_COUNT = 5
API_KEY = 'lNP5pbeh5OIfQa5fsjaZroXmsX4E9JGA'
# search_query = 'election'


def get_articles(search_query):
    page = requests.get(
        'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=%s&api-key=%s' % (search_query, API_KEY))
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup.find('docs'))
    data = json.loads(str(soup))
    # print(data.get("docs"))
    full_response = data.get('response')
    if full_response:
        docs = full_response.get('docs')
        # print(docs)
        if len(docs) > ARTICLE_COUNT:
            docs = docs[:ARTICLE_COUNT]

        news_items = list()
        for doc in docs:
            article = Article(
                _headline=doc.get('headline').get('main'),
                _author=doc.get('byline').get('original'),
                _url=doc.get('web_url'),
                _lead=doc.get('lead_paragraph'),
                _abstract=doc.get('abstract'),
                _timestamp=doc.get('pub_date').split('T')[0]
            )
            news_items.append(article)



            # news_item = dict()
            # news_item['headline'] = doc.get('headline').get('main')
            # news_item['url'] = doc.get('web_url')
            # news_item['abstract'] = doc.get('abstract')
            # news_item['lead_paragraph'] = doc.get('lead_paragraph')
            # news_item['author'] = doc.get('byline').get('original')
            # news_item['timestamp'] = doc.get('pub_date').split('T')[0]
            # news_items.append(news_item)
        return news_items


def index(request):
    return render(request, "top_five/index.html")


class ArticleSearchListView(ListView):
    template_name = 'top_five/search_results.html'

    def get_queryset(self):
        # result = super(ArticleSearchListView).get_queryset()
        query_string = self.request.GET.get('query')
        # Save query to db here
        if query_string:
            query = Query(title=query_string)
            query.save()
            articles = get_articles(query)
            return articles

