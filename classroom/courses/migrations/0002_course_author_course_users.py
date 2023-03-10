# Generated by Django 4.1.6 on 2023-03-10 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='courses_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='users',
            field=models.ManyToManyField(related_name='courses_student', to=settings.AUTH_USER_MODEL, verbose_name='Студенты'),
        ),
    ]
