from django.conf.urls import url
from django.contrib import admin
from myapp import views

urlpatterns = [
    url(r'cs/$', views.viewIndex.as_view(), name='cs'),
]