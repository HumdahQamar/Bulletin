from django.urls import path

from top_five import views


urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.ArticleSearchListView.as_view(), name='search_results'),
]