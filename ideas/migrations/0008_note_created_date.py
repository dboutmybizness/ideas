# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0007_idea_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]
