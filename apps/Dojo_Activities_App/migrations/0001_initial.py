# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-08 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=222)),
                ('startdatetime', models.DateTimeField()),
                ('enddatetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=222)),
                ('alias', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='coordinator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coordinator', to='Dojo_Activities_App.User'),
        ),
        migrations.AddField(
            model_name='activity',
            name='participant',
            field=models.ManyToManyField(related_name='participant', to='Dojo_Activities_App.User'),
        ),
    ]