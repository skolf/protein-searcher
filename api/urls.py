from django.urls import path

from . import views

urlpatterns = [
    path('searches', views.SearchList.as_view(), name='list'),
]
