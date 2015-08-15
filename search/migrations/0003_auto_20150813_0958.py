# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20150718_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.ForeignKey(to='search.Artist', related_name='songs'),
        ),
    ]
