# Generated by Django 4.1.7 on 2023-03-17 16:51

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='static/default.jpeg', upload_to=core.utils.user_directory_path, verbose_name='Фото профиля'),
        ),
    ]
