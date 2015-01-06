# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Player_Id', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('DOB', models.DateTimeField(verbose_name=b'Date of birth')),
                ('registration_date', models.DateTimeField(verbose_name=b'Date of Registration')),
                ('gender', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.IntegerField(default=0)),
                ('mobile', models.IntegerField(max_length=12)),
                ('email', models.EmailField(max_length=75)),
                ('question', models.CharField(max_length=100)),
                ('last_club_played', models.CharField(max_length=50)),
                ('last_league', models.CharField(max_length=100)),
                ('date_last_register', models.DateTimeField(verbose_name=b'Date of lastreg')),
                ('date_last_played', models.DateTimeField(verbose_name=b'Date of lastplayed')),
                ('salary', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
