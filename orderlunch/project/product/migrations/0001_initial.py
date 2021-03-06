# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trademark', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Title')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('trademark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trademarks', to='trademark.Trademark')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id',)]),
        ),
    ]
