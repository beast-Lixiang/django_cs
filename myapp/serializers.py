# -*- coding:utf8 -*-
from rest_framework import serializers
from myapp.models import indexView


class filmserializers(serializers.ModelSerializer):
    filmId = serializers.CharField(help_text="电影Id", source='extInfo.filmId')
    filmName = serializers.CharField(help_text=u"电影名字", source='extInfo.filmName')
    class Meta:
        model = indexView