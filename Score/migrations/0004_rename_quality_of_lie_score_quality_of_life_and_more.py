# Generated by Django 4.0.4 on 2022-05-11 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cities', '0003_alter_cities_citi_main_slug_alter_cities_country_and_more'),
        ('Score', '0003_rename_rate_field_score_air_quality_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='quality_of_lie',
            new_name='quality_of_life',
        ),
        migrations.AlterField(
            model_name='score',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score', to='Cities.listofcities', unique=True),
        ),
    ]
