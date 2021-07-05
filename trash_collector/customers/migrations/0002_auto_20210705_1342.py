# Generated by Django 3.1.8 on 2021-07-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default=' ', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='end_suspension',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='onetime_pickup',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='start_suspension',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='weekly_pickup_day',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='zip_code',
            field=models.CharField(default=' ', max_length=5),
            preserve_default=False,
        ),
    ]
