# Generated by Django 3.2.7 on 2021-10-10 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0025_auto_20211010_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likenew',
            name='new',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.new'),
        ),
    ]