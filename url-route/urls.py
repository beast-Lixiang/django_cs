from django.conf.urls import url, include
from django.contrib import admin
from myapp import views

urlpatterns = [
    url(r'^film_name/$', views.viewIndex.as_view(), name='film'),

]