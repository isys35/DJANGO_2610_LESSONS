from django.db import models
from user_role.models import User


class Student(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
