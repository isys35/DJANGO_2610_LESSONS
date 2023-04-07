# Generated by Django 4.1.7 on 2023-04-07 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название темы')),
                ('hours', models.PositiveIntegerField(verbose_name='Количество часов')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Порядок')),
                ('road_map', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='roadmaps.roadmap', verbose_name='Программа обучения')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
                'ordering': ['order', 'name'],
            },
        ),
    ]