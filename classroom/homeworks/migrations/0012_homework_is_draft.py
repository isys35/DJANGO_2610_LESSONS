# Generated by Django 4.1.6 on 2023-02-17 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0011_alter_homework_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='is_draft',
            field=models.BooleanField(default=False, verbose_name='Это черновик'),
        ),
    ]
