# Generated by Django 4.0.4 on 2022-06-04 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cities', '0007_alter_countries_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cities',
            options={'ordering': ['citi_main_slug']},
        ),
    ]
