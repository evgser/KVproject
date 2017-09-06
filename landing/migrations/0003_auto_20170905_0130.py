# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-04 22:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20170828_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='account_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Account', verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.City', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='gameinfo',
            name='game_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Game', verbose_name='ID игры'),
        ),
        migrations.AlterField(
            model_name='person',
            name='account_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.City', verbose_name='Город'),
        ),
    ]
