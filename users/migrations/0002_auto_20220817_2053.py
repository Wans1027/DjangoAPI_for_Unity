# Generated by Django 3.1.6 on 2022-08-17 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='position',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='subjects',
        ),
    ]