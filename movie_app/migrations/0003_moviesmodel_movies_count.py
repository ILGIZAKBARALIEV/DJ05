# Generated by Django 5.1.6 on 2025-03-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_remove_moviesmodel_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviesmodel',
            name='movies_count',
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
    ]
