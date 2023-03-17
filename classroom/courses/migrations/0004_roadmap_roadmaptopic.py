# Generated by Django 4.1.7 on 2023-03-17 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoadMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название программы')),
            ],
            options={
                'verbose_name': 'Программа обучения',
                'verbose_name_plural': 'Программы обучения',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RoadMapTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название темы')),
                ('hours', models.PositiveIntegerField(verbose_name='Количество часов')),
                ('road_map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.roadmap', verbose_name='Программа обучения')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
                'ordering': ['name'],
            },
        ),
    ]
