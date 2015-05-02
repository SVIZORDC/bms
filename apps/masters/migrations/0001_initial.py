# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('company', models.ForeignKey(to='accounts.Company')),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'release_masters')),
            ],
        ),
        migrations.CreateModel(
            name='SourceMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'source_masters')),
                ('project', models.ForeignKey(to='masters.Project')),
            ],
        ),
        migrations.AddField(
            model_name='releasemaster',
            name='source_master',
            field=models.ForeignKey(to='masters.SourceMaster'),
        ),
    ]
