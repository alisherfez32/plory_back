# Generated by Django 4.0.4 on 2022-06-11 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Countries', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countries',
            old_name='location',
            new_name='continent',
        ),
        migrations.RemoveField(
            model_name='countries',
            name='population',
        ),
    ]
