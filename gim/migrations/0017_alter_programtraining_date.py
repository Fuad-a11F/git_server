# Generated by Django 3.2.7 on 2021-10-01 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gim', '0016_auto_20211001_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programtraining',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
