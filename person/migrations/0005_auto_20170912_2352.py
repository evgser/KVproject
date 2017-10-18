# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_auto_20170912_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.City', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=32, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=32, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.IntegerField(null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='person',
            name='sub_email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Доп. эл. почта'),
        ),
    ]
