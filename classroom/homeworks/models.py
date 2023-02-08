from django.db import models


class Homework(models.Model):
    class TypeChoices(models.TextChoices):
        TASK = "task", "Задача"
        REFACTOR = "refactor", "Рефакторинг"
        TESTS = "tests", "Тесты"
        OTHER = "other"
        __empty__ = "Выберите значение"

    topic = models.ForeignKey(
        'Topic',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Тема",
        related_name="homeworks",
        related_query_name="homeworks"
    )
    type = models.CharField(max_length=15, choices=TypeChoices.choices, blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(blank=True, verbose_name="Описание")
    mark = models.PositiveIntegerField(default=10, verbose_name="Максимальная оценка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    deadline = models.DateTimeField(null=True, blank=True, verbose_name="Дэдлайн")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Домашнее задание"
        verbose_name_plural = "Домашние задания"
        ordering = ["-created_at"]


class Topic(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название темы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"
