from __future__ import unicode_literals

from django.db import models


class IndexView(models.Model):
    filmId = models.CharField(max_length=12)
    filmName = models.CharField(max_length=12)

    @property
    def filmInfo(self):
        return self.filmId + "  " + self.filmName

    def __str__(self):
        return self.filmName

    class Meta:
        db_table = 'film_name'


    @classmethod
    def create_one_record(cls, id, name):
        record = IndexView.objects.create(filmId=id, filmName=name)
        record.save()


    @classmethod
    def get_one_record(cls, name):
        record =IndexView.objects.filter(filmName=name)
        return record