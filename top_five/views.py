import json
import requests

from bs4 import BeautifulSoup
from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Query
from top_five.helpers.article import Article


ARTICLE_COUNT = 5
API_KEY = 'lNP5pbeh5OIfQa5fsjaZroXmsX4E9JGA'


def get_articles(search_query):
    page = requests.get(
        'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=%s&api-key=%s' % (search_query, API_KEY)
    )
    soup = BeautifulSoup(page.text, 'html.parser')
    data = json.loads(str(soup))
    full_response = data.get('response')
    if full_response:
        docs = full_response.get('docs')
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
                _timestamp=doc.get('pub_date').split('T')[0],
                _query=search_query
            )
            news_items.append(article)
        return news_items


def index(request):
    queries = Query.objects.all()
    return render(
        request,
        "top_five/base.html",
        {
            'queries': queries,
        }
    )


class ArticleSearchDetailView(DetailView):
    model = Query
    template_name = 'top_five/search_results.html'

    def get_context_data(self, **kwargs):
        context = dict()
        query = Query.objects.get(pk=self.kwargs.get('pk'))
        if query:
            context['articles'] = get_articles(query.title)
            context['current_query'] = query.title
            return context
