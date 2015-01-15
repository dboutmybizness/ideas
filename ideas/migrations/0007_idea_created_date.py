# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0006_auto_20150114_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='created_date',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]
