from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
