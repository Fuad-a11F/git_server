# Generated by Django 3.2.7 on 2021-10-08 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gim', '0024_draftfood'),
    ]

    operations = [
        migrations.AddField(
            model_name='programfood',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
    ]