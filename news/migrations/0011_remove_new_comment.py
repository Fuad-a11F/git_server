# Generated by Django 3.2.7 on 2021-09-30 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20210923_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='comment',
        ),
    ]
