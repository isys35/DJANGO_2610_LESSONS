# Generated by Django 4.1.6 on 2023-02-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='mark',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
