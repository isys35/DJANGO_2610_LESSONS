from django.db import models
from user_role.models import AbstractUser

from core.utils import user_directory_path


class User(AbstractUser):
    photo = models.ImageField(verbose_name="Фото профиля", default="static/default.jpeg", upload_to=user_directory_path)


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="info")
    country = models.CharField(max_length=100, verbose_name="Страна", blank=True)
    post_code = models.CharField(max_length=100, verbose_name="Почтовый индекс", blank=True)
