# Generated by Django 4.0.4 on 2022-05-25 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0013_alter_countryfood_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
