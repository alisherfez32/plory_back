# Generated by Django 4.0.4 on 2022-06-11 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Countries', '0003_alter_countries_continent'),
        ('Apps', '0012_alter_commonapps_options_commonapps_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countryapps',
            name='country',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='Countries.countries'),
        ),
        migrations.AlterField(
            model_name='countryapps',
            name='slug',
            field=models.SlugField(blank=True, default=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='Countries.countries')),
        ),
    ]
