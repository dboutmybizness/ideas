# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0008_note_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='created_date',
        ),
    ]
