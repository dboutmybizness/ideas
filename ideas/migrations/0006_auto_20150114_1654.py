# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0005_auto_20141228_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='full_description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='idea',
            name='idea_type',
            field=models.ForeignKey(blank=True, to='ideas.Idea_Type', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='idea',
            name='short_description',
            field=models.CharField(max_length=254, blank=True),
            preserve_default=True,
        ),
    ]
