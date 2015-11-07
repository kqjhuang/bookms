# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isbn', models.CharField(unique=True, max_length=13, verbose_name=b'ISBN')),
                ('title', models.CharField(max_length=200, verbose_name=b'\xe4\xb9\xa6\xe5\x90\x8d')),
                ('subtitle', models.CharField(max_length=200, verbose_name=b'\xe5\x89\xaf\xe6\xa0\x87\xe9\xa2\x98', blank=True)),
                ('pages', models.IntegerField(verbose_name=b'\xe9\xa1\xb5\xe6\x95\xb0', blank=True)),
                ('author', models.CharField(max_length=60, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('translator', models.CharField(max_length=60, verbose_name=b'\xe8\xaf\x91\xe8\x80\x85', blank=True)),
                ('price', models.CharField(max_length=60, verbose_name=b'\xe5\xae\x9a\xe4\xbb\xb7', blank=True)),
                ('publisher', models.CharField(max_length=200, verbose_name=b'\xe5\x87\xba\xe7\x89\x88\xe7\xa4\xbe', blank=True)),
                ('pubdate', models.CharField(max_length=60, verbose_name=b'\xe5\x87\xba\xe7\x89\x88\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('cover_img', models.URLField(verbose_name=b'\xe5\xb0\x81\xe9\x9d\xa2\xe5\x9b\xbe', blank=True)),
                ('summary', models.TextField(max_length=2000, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9\xe7\xae\x80\xe4\xbb\x8b', blank=True)),
                ('author_intro', models.TextField(max_length=2000, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85\xe7\xae\x80\xe4\xbb\x8b', blank=True)),
            ],
            options={
                'verbose_name': '\u56fe\u4e66',
                'verbose_name_plural': '\u56fe\u4e66',
            },
        ),
    ]
