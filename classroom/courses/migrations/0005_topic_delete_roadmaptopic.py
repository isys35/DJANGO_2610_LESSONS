# Generated by Django 4.1.7 on 2023-03-22 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_roadmap_roadmaptopic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название темы')),
                ('hours', models.PositiveIntegerField(verbose_name='Количество часов')),
                ('road_map', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='courses.roadmap', verbose_name='Программа обучения')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='RoadMapTopic',
        ),
    ]