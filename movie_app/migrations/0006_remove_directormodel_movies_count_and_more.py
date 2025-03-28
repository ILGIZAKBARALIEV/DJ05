# Generated by Django 5.1.6 on 2025-03-11 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_remove_reviewmodel_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='directormodel',
            name='movies_count',
        ),
        migrations.AlterField(
            model_name='moviesmodel',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movie_app.directormodel'),
        ),
    ]
