# -*- coding:utf8 -*-
from rest_framework import serializers
from myapp.models import IndexView


class FilmSerializers(serializers.ModelSerializer):
    filmId = serializers.CharField(help_text=u"电影Id")
    filmName = serializers.CharField(help_text=u"电影名字")
    class Meta:
        model = IndexView
        exclude = ('id',)#去掉多余的项
