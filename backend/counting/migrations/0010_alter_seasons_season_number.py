# Generated by Django 4.2.3 on 2023-08-02 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counting', '0009_alter_seasons_season_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seasons',
            name='season_number',
            field=models.IntegerField(unique=True),
        ),
    ]
