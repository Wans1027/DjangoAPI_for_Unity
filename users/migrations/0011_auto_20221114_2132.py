# Generated by Django 3.1.6 on 2022-11-14 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_profile_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='position',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='subjects',
        ),
    ]