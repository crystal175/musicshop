# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20150813_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=30)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('comment', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('song', models.ForeignKey(to='search.Song', related_name='orders')),
            ],
        ),
    ]
