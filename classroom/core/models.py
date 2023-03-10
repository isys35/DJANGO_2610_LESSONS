from django.contrib.auth.models import AbstractUser
from django.db import models

from core.managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField("Email", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

