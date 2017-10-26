# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-07 22:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '__first__'),
        ('landing', '0006_auto_20170908_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=32, verbose_name='Пароль от игры')),
            ],
            options={
                'verbose_name': 'Созданная игра',
                'verbose_name_plural': 'Созданные игры',
            },
        ),
        migrations.CreateModel(
            name='GameInfo',
            fields=[
                ('game', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='game.Game', verbose_name='ID игры')),
                ('name', models.CharField(default='name', max_length=16, verbose_name='Название игры')),
                ('info', models.TextField(verbose_name='Описание игры')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.City', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Информация об игре',
                'verbose_name_plural': 'Информация об играх',
            },
        ),
        migrations.AddField(
            model_name='game',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='person.Person', verbose_name='Логин'),
        ),
    ]