# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0004_auto_20141228_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='full_description',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idea',
            name='short_description',
            field=models.CharField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='idea_type',
            name='idea_industry',
            field=models.CharField(max_length=25, choices=[(b'TECHNOLOGY', b'Technology'), (b'MASS_MEDIA', b'Mass Media')]),
            preserve_default=True,
        ),
    ]
