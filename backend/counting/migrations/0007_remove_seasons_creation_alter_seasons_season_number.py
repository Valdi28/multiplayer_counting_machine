# Generated by Django 4.2.3 on 2023-08-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counting', '0006_seasons_delete_count_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seasons',
            name='creation',
        ),
        migrations.AlterField(
            model_name='seasons',
            name='season_number',
            field=models.IntegerField(unique=True),
        ),
    ]