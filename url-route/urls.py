from django.conf.urls import url, include
from django.contrib import admin
from myapp import views

urlpatterns = [
    url(r'^film_name/$', views.viewIndex.as_view(), name='film'),
    url(r'^film_name/(?P<pk>[0-9]+)/', views.ViewOneIndex.as_view(), name='film_only'),
    url(r'^film_name/(?P<pstr>[a-z]+)/', views.ViewOneFilmName.as_view(), name='film_name')

]