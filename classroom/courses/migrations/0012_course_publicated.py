# Generated by Django 4.1.7 on 2023-04-05 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_comment_likes_alter_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='publicated',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
    ]
