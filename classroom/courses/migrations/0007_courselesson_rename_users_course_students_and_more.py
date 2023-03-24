# Generated by Django 4.1.7 on 2023-03-24 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0006_alter_topic_options_topic_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Тема занятия')),
                ('started_at', models.DateTimeField(verbose_name='Начало занятия')),
            ],
            options={
                'verbose_name': 'Занятие',
                'verbose_name_plural': 'Занятия',
                'ordering': ['started_at'],
            },
        ),
        migrations.RenameField(
            model_name='course',
            old_name='users',
            new_name='students',
        ),
        migrations.CreateModel(
            name='StudentLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('not_completed', 'Не пройден'), ('completed', 'Пройден')], default='not_completed', max_length=20, verbose_name='Статус')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courselesson', verbose_name='Занятие')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Учащийся')),
            ],
            options={
                'verbose_name': 'Занятие учащегося',
                'verbose_name_plural': 'Занятия учащихся',
                'ordering': ['student', 'lesson'],
            },
        ),
        migrations.AddField(
            model_name='courselesson',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course', verbose_name='Курс'),
        ),
        migrations.AddField(
            model_name='courselesson',
            name='students',
            field=models.ManyToManyField(through='courses.StudentLesson', to=settings.AUTH_USER_MODEL),
        ),
    ]