# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_idea_created_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idea_type', models.CharField(max_length=50)),
                ('idea_industry', models.CharField(max_length=25, choices=[(b'TECHNOLOGY', b'Technology')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='idea',
            name='idea_type',
            field=models.ForeignKey(to='ideas.Idea_Type', null=True),
            preserve_default=True,
        ),
    ]
