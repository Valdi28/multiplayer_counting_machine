# Generated by Django 4.2.3 on 2023-07-30 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='count',
            name='creation',
            field=models.TextField(),
        ),
    ]
