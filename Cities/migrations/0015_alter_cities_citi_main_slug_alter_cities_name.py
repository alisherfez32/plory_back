# Generated by Django 4.0.4 on 2022-06-11 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cities', '0014_districts_rename_airstatus_airports_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='citi_main_slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cities',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_of_city', to='Cities.listofcities'),
        ),
    ]