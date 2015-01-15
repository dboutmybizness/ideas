# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0011_idea_initial_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='headline',
            field=models.CharField(default=None, max_length=140, blank=True),
            preserve_default=False,
        ),
    ]
