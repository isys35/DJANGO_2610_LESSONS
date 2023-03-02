from django.db import models
from django.urls import reverse_lazy

from courses import validators


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название курса")
    description = models.TextField(blank=True, verbose_name="Описание")
    started_at = models.DateField(verbose_name="Старт курса")

    def get_absolute_url(self):
        return reverse_lazy("courses:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["-started_at"]
