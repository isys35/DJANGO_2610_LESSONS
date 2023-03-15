from django.db import models
from user_role.models import AbstractUser


class User(AbstractUser):
    ...


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="info")
    country = models.CharField(max_length=100, verbose_name="Страна", blank=True)
    post_code = models.CharField(max_length=100, verbose_name="Почтовый индекс", blank=True)
