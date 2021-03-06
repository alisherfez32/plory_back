# Generated by Django 4.0.4 on 2022-06-11 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Countries', '0005_delete_religions_alter_countries_independence_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='airports',
            name='airport_slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seasons',
            name='season_slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seasons',
            name='name',
            field=models.CharField(max_length=201),
        ),
    ]
