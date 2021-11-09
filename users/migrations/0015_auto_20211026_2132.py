# Generated by Django 3.2.7 on 2021-10-26 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20211023_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='time_begin_work',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='time_finish_work',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='time_visit_gim',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='experience',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
