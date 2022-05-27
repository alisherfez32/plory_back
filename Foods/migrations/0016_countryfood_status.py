# Generated by Django 4.0.4 on 2022-05-25 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0015_remove_countryfood_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='countryfood',
            name='status',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='Foods.status'),
        ),
    ]