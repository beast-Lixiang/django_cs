# -*- coding:utf-8 -*-
from django.shortcuts import render
from rest_framework import generics, mixins, status, permissions
from rest_framework.response import Response
from myapp.models import IndexView
from django.db.models import Q
from myapp.serializers import FilmSerializers


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
            - code: 404
              message: Not Found Page
        """
        dict = self.request.query_params
        query = Q()
        if dict.get('search'):
            query &= Q(filmId__icontains=dict.get('search'))
            query |= Q(filmName__icontains=dict.get('search'))
        record = IndexView.objects.filter(query)
        return Response([[obj.filmId, obj.filmName] for obj in record])




    def post(self, request):
        """
        新增电影
        ---
        :param request:
        :param filmId:
        :param filmName:
        :return:

        response_serializer: FilmSerializers
        many: True

        parameters:
            - name: film_id
              description: 电影id
              type: string
              paramType: query
              # required: False
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
            record = IndexView.objects.create(filmId=filmid, filmName=filmname)
        p = FilmSerializers(record)

        return Response(p.data)


class ViewOneIndex(generics.ListAPIView):


    def get(self, request, pk):
        """
        获得单个电影
        ---
        :param request:
        :param args:
        :param kwargs:
        :return:
        response_serializer: FilmSerializers
        many: False
        parameter:
              - name: id
                description: 电影id
                type: int
                paramType: query

        responseMessages:
            - code: 401
              message: Not authenticated
        """
        record = IndexView.objects.filter(id=pk).first()
        p = FilmSerializers(record)
        return Response(p.data)


class ViewOneFilmName(generics.ListAPIView):


    def get(self, request, pstr):
        """
        通过电影名
        ---
        :param request:
        :param pstr:
        :return:
        response_serializer: FilmSerializers
        many: False
        parameter:
              - name: name
                description: 电影名
                type: int
                paramType: query

        responseMessages:
            - code: 401
              message: Not authenticated
        """
        record = IndexView.objects.filter(filmName=pstr).first()
        p = FilmSerializers(record)
        return Response(p.data)