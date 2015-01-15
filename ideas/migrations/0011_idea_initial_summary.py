# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0010_auto_20150114_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='initial_summary',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
