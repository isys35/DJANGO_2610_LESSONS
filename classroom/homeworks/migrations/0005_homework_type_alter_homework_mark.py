# Generated by Django 4.1.6 on 2023-02-08 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0004_alter_homework_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='type',
            field=models.CharField(choices=[('task', 'Задача'), ('refactor', 'Рефакторинг'), ('tests', 'Тесты')], default='task', max_length=10),
        ),
        migrations.AlterField(
            model_name='homework',
            name='mark',
            field=models.PositiveIntegerField(default=10, verbose_name='Максимальная оценка'),
        ),
    ]
