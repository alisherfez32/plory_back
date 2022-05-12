# Generated by Django 4.0.4 on 2022-05-11 07:50

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Score', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scorestatus',
            name='rate_field',
        ),
        migrations.AddField(
            model_name='score',
            name='rate_field',
            field=models.DecimalField(decimal_places=0, default=Decimal('0'), max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
