# coding=utf-8

from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'Название', max_length=64)
    author = models.CharField(u'Автор', max_length=64)
    pub_date = models.DateField(u'Дата публикации')

    # ограничение повторяющихся значений в таблице (если совпадут все поля)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['name', 'author', 'pub_date'], name='unique_book')]

    def __str__(self):
        return self.name + " " + self.author
