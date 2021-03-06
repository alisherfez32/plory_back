# Generated by Django 4.0.4 on 2022-06-11 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cities', '0011_remove_cities_country_delete_countries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('country_slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cities',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Cities.countries'),
        ),
    ]
