# coding:utf-8
from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField('帐号', max_length=20, unique=True)
    password = models.CharField('密码', max_length=15)

    def __unicode__(self):
        return self.name
