# Generated by Django 3.2.7 on 2021-09-30 04:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0014_auto_20210930_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='like_new_comment',
            field=models.ManyToManyField(blank=True, default='0', null=True, related_name='like_new_comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like_new_comment',
        ),
    ]
