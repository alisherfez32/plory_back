# Generated by Django 4.0.4 on 2022-06-18 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0002_alter_commonapps_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='filters',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]
