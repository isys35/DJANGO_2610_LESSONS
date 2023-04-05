from django.db import models


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
        return f"{self.name} {self.hours} часов"

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"
        ordering = ["order", "name"]
