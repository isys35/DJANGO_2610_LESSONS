# Generated by Django 4.1.7 on 2023-04-07 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roadmaps', '0001_initial'),
        ('courses', '0012_course_publicated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='road_map',
        ),
        migrations.AlterField(
            model_name='course',
            name='road_map',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses', to='roadmaps.roadmap', verbose_name='Программа обучение'),
        ),
        migrations.DeleteModel(
            name='RoadMap',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]