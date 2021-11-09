# Generated by Django 3.2.7 on 2021-10-09 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0016_alter_favoritemusic_music'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='music',
        ),
        migrations.AddField(
            model_name='music',
            name='playlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.playlist'),
        ),
    ]
