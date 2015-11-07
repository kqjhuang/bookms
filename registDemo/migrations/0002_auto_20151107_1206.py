# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registDemo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(unique=True, max_length=20, verbose_name=b'\xe5\xb8\x90\xe5\x8f\xb7'),
        ),
    ]
