from django.db import models
from django.urls import reverse_lazy


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название курса")
    description = models.TextField(blank=True, verbose_name="Описание")
    started_at = models.DateField(verbose_name="Старт курса")
    author = models.ForeignKey(
        "core.User",
        verbose_name="Автор",
        on_delete=models.PROTECT,
        related_name="courses_author",
        blank=True,
        null=True
    )
    users = models.ManyToManyField(
        "core.User", verbose_name="Студенты", related_name="courses_student"
    )

    def get_absolute_url(self):
        return reverse_lazy("courses:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["-started_at"]


class RoadMap(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название программы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Программа обучения"
        verbose_name_plural = "Программы обучения"
        ordering = ["name"]


class Topic(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название темы")
    road_map = models.ForeignKey(
        RoadMap,
        on_delete=models.CASCADE,
        verbose_name="Программа обучения",
        related_name="topics",
        blank=True,
        null=True,
    )
    hours = models.PositiveIntegerField(verbose_name="Количество часов")
    order = models.SmallIntegerField(verbose_name="Порядок", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"
        ordering = ["order", "name"]
