# Generated by Django 3.2.7 on 2021-10-23 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0006_auto_20211005_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTrainingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProgramFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('text', models.CharField(max_length=200)),
                ('isNew', models.BooleanField(default=True)),
                ('isActive', models.BooleanField(default=False)),
                ('foodItems', models.ManyToManyField(to='food.FoodTrainingItem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userF', to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DraftFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=250)),
                ('programItems', models.ManyToManyField(to='food.FoodTrainingItem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userDF', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
