# Generated by Django 4.0.4 on 2022-06-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0011_alter_commonapps_description_alter_commonapps_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commonapps',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='commonapps',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]