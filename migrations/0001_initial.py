# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=254, blank=True)),
                ('full_description', models.TextField(blank=True)),
                ('initial_summary', models.TextField(null=True, blank=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Idea_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idea_type', models.CharField(max_length=50)),
                ('idea_industry', models.CharField(max_length=25, choices=[(b'TECHNOLOGY', b'Technology'), (b'MASS_MEDIA', b'Mass Media'), (b'GEN', b'General')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=140, blank=True)),
                ('txt', models.TextField()),
                ('created_date', models.DateField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('idea', models.ForeignKey(to='ideas.Idea')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='idea',
            name='idea_type',
            field=models.ForeignKey(blank=True, to='ideas.Idea_Type', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='idea',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
