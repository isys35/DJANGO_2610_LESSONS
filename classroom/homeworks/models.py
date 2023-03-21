from django.db import models
from core import models as core_models


class DeletedHomeworks(models.Model):
    deleted_at = models.DateTimeField(auto_now_add=True, verbose_name="Удалено")
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(blank=True, verbose_name="Описание")


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
    is_draft = models.BooleanField(default=False, verbose_name="Это черновик")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/homeworks/{self.pk}"

    def full_info(self):
        return f"Наименование задания: {self.name}"

    full_info.short_description = "Полное наименование"

    class Meta:
        verbose_name = "Домашнее задание"
        verbose_name_plural = "Домашние задания"
        ordering = ["-created_at", "name"]
        # unique_together = ("type", "name")
        get_latest_by = "created_at"
        constraints = (
            models.CheckConstraint(
                check=models.Q(mark__lte=1000),
                name="%(app_label)s_%(class)s_max_mark_constraint"
            ),
            models.UniqueConstraint(
                fields=("name", "type"),
                condition=models.Q(type__isnull=False),
                name="%(app_label)s_%(class)s_name_type_unique_constraint"
            )
        )


class Topic(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название темы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"
