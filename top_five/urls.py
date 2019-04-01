from django.urls import path

from top_five import views


urlpatterns = [
    path('', views.index, name='index'),
]