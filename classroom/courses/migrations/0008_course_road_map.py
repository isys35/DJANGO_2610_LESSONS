# Generated by Django 4.1.7 on 2023-03-24 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_courselesson_rename_users_course_students_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='road_map',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses', to='courses.roadmap', verbose_name='Программа обучение'),
        ),
    ]