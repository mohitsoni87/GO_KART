# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Seller_Username', models.CharField(max_length=100, null=True)),
                ('Category', models.CharField(max_length=100)),
                ('Company_Name', models.CharField(max_length=100)),
                ('Product_Name', models.CharField(max_length=100)),
                ('Price', models.CharField(max_length=10)),
                ('Product_Image', models.FileField(max_length=1000, null=True, upload_to=b'')),
            ],
        ),
    ]
