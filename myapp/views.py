# -*- coding:utf-8 -*-
from django.shortcuts import render
from rest_framework import generics, mixins, status, permissions
from rest_framework.response import Response
from myapp.models import indexView
from django.db.models import Q
from myapp.serializers import filmserializers


class viewIndex(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        """
        电影列表
        ---
        :param request:
        :param args:
        :param kwargs:
        :return:
        parameters:
            - name: search
              description: 电影名
              type: string
              paramType: query
        responseMessages:
            - code: 401
              message: Not authenticated
        """
        dict = self.request.query_params
        query = Q()
        if dict.get('search'):
            query &= Q(filmId__icontains=dict.get('search'))
            query |= Q(filmName__icontains=dict.get('search'))
        record = indexView.objects.filter(query)
        return Response([[obj.filmId, obj.filmName] for obj in record])




    def post(self, request):
        """
        新增电影
        ---
        :param request:
        :param filmId:
        :param filmName:
        :return:

        serializer: filmserializers
        many: false

        parameters:
            - name: film_id
              description: 电影id
              type: string
              paramType: query
            - name: film_name
              description: 电影名
              type: string
              paramType: query
        responseMessages:
            - code: 401
              message: Not authenticated
        """
        dict = self.request.query_params
        filmid = dict.get('film_id')
        filmname = dict.get('film_name')
        if filmname and filmid:
            record = indexView.objects.create(filmId=filmid, filmName=filmname).save()

        return Response(record)