# Generated by Django 4.0.4 on 2022-05-11 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cities', '0003_alter_cities_citi_main_slug_alter_cities_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='search',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='countries',
            name='search',
            field=models.TextField(blank=True, default='', editable=False),
        ),
    ]