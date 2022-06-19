# Generated by Django 4.0.4 on 2022-06-19 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cities', '0015_alter_cities_citi_main_slug_alter_cities_name'),
        ('CostOfLiving', '0008_alter_costs_options_costs_filter_by_costs_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costs',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cost_of_living', to='Cities.listofcities'),
        ),
    ]
