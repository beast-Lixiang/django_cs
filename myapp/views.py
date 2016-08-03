from django.shortcuts import render
from rest_framework import generics, mixins, status, permissions

# Create your views here.
class viewIndex(generics.ListAPIView):



    def post(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super(viewIndex, self).post(request, *args, **kwargs)
