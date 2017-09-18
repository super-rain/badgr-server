# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-18 14:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0031_auto_20170918_0735'),
    ]

    operations = [
        migrations.CreateModel(
            name='BadgeClassTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=254)),
                ('badgeclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issuer.BadgeClass')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
