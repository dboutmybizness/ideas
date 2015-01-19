# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ideas', '0012_note_headline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recently_Viewed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('viewed_time', models.DateTimeField()),
                ('idea', models.ForeignKey(to='ideas.Idea')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='idea_type',
            name='idea_industry',
            field=models.CharField(max_length=25, choices=[(b'TECHNOLOGY', b'Technology'), (b'MASS_MEDIA', b'Mass Media'), (b'GEN', b'General')]),
            preserve_default=True,
        ),
    ]
