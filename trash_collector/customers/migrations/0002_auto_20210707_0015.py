# Generated by Django 3.1.8 on 2021-07-07 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='weekly_pickup_day',
            field=models.CharField(max_length=9),
        ),
    ]
