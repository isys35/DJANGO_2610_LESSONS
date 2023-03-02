from django.contrib.auth.models import Permission
from django.db import models


class PermissionProxy(Permission):

    def __str__(self):
        return self.codename

    class Meta:
        proxy = True
