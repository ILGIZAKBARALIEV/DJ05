# Generated by Django 5.1.6 on 2025-03-11 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_alter_reviewmodel_movies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewmodel',
            name='reviews',
        ),
    ]
