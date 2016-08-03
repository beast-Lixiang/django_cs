# coding=utf-8
from distutils.util import strtobool
from rest_framework.fields import BooleanField
from rest_framework import serializers, fields, pagination
from rest_framework.response import Response

from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        return request.user.is_staff


class JsonPropertyField(serializers.Field):
    def get_attribute(self, instance):
        """
        Given the *outgoing* object instance, return the primitive value
        that should be used for this field.
        """
        try:
            return fields.get_attribute(instance, self.source_attrs)
        except (KeyError, AttributeError) as exc:
            return None if self.default == fields.empty else self.default

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data


class BooleanJsonPropertyField(BooleanField):

    def get_attribute(self, instance):
        """
        Given the *outgoing* object instance, return the primitive value
        that should be used for this field.
        """
        try:
            return fields.get_attribute(instance , self.source_attrs)
        except (KeyError , AttributeError) as exc:
            return None if self.default == fields.empty else self.default

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return strtobool(data)


class PointField(serializers.Field):
    def to_internal_value(self, data):
        return data

    def __init__(self, **kwargs):
        kwargs['read_only'] = True
        super(PointField, self).__init__(**kwargs)

    def to_representation(self, value):
        return (value.x, value.y)


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'

    def get_paginated_data(self, data):
        return {
            'page': self.page.number,
            'page_size': self.page_size,
            'has_next': self.page.paginator.num_pages > self.page.number,
            'count': self.page.paginator.count,
            'results': data
        }

    def get_paginated_response(self, data):
        return Response(self.get_paginated_data(data))

    def get_paginated_response_with_ext(self, data, **kwargs):
        data = self.get_paginated_data(data)
        if kwargs:
            data.update(**kwargs)
        return data


class PaginationSerializer(serializers.Serializer):
    page = serializers.IntegerField(help_text=u"页数", read_only=True)
    page_size = serializers.IntegerField(help_text=u"每页页数", read_only=True)
    count = serializers.IntegerField(help_text=u"总数", read_only=True)
    has_next = serializers.BooleanField(help_text=u"是否有下一页", read_only=True)
