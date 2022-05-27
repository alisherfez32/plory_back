# Generated by Django 4.0.4 on 2022-05-25 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0006_remove_countryapps_search_countryapps_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commonapps',
            name='url',
        ),
        migrations.AddField(
            model_name='commonapps',
            name='android_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='commonapps',
            name='ios_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
