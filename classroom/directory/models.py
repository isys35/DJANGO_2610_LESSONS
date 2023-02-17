from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="child",
        null=True,
        blank=True
    )
