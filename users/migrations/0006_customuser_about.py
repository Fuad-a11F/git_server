# Generated by Django 3.2.7 on 2021-10-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_paid_customuser_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
