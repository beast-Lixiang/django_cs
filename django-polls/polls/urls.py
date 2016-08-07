from django.conf.urls import url
from polls import views


urlpatterns = [
    url(r'^a$', views.IndexView.as_view(), name="polls"),
    url(r'^b$', views.index_1, name="polls_1"),
    url(r'^c$', views.index_2, name="polls_2"),
    url(r'^(?P<question_id>[0-9]+)/detail_3$', views.detail_1, name="detail_3"),
    url(r'^(?P<question_id>[0-9]+)/detail_2$', views.detail_1, name="detail_2"),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]

