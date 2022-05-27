# Generated by Django 4.0.4 on 2022-05-25 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0003_countryfood_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
