# Generated by Django 5.0.7 on 2024-08-03 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0004_rename_subcategory_id_place_subcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='route_places',
            old_name='route_id',
            new_name='route',
        ),
        migrations.AddField(
            model_name='route',
            name='places',
            field=models.ManyToManyField(related_name='routes', through='route.Route_places', to='route.place'),
        ),
        migrations.AddField(
            model_name='route_places',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='route.place'),
        ),
    ]