# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-07 22:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.BooleanField(verbose_name='Роль')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Название команды')),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Person', verbose_name='Лидер')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
        migrations.AddField(
            model_name='personteam',
            name='team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.Team'),
        ),
    ]