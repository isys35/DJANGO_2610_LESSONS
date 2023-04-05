from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse_lazy

from courses import managers
from courses import consts


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
    students = models.ManyToManyField(
        "core.User", verbose_name="Студенты", related_name="courses_student"
    )
    road_map = models.ForeignKey(
        "RoadMap",
        on_delete=models.SET_NULL,
        verbose_name="Программа обучение",
        related_name="courses",
        blank=True,
        null=True
    )
    publicated = models.BooleanField(default=False, verbose_name="Опубликовано")
    comments = GenericRelation("Comment")

    objects = models.Manager()
    active_objects = managers.PublicatedManager()
    with_count_objects = managers.QuerySetCountStudent.as_manager()

    def get_absolute_url(self):
        return reverse_lazy("courses:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["-started_at"]


class CourseLesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="lessons",
        verbose_name="Курс"
    )
    name = models.TextField(verbose_name="Тема занятия")
    started_at = models.DateTimeField(verbose_name="Начало занятия")
    students = models.ManyToManyField("core.User", through="StudentLesson")
    comments = GenericRelation("Comment")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"
        ordering = ["started_at"]


class StudentLesson(models.Model):
    lesson = models.ForeignKey(CourseLesson, on_delete=models.CASCADE, verbose_name="Занятие")
    student = models.ForeignKey("core.User", on_delete=models.CASCADE, verbose_name="Учащийся")
    status = models.CharField(
        max_length=20,
        verbose_name="Статус",
        choices=consts.StudentLessonStatus.choices,
        default=consts.StudentLessonStatus.NOT_COMPLETED
    )

    def __str__(self):
        return f"{self.lesson} {self.student}"

    class Meta:
        verbose_name = "Занятие учащегося"
        verbose_name_plural = "Занятия учащихся"
        ordering = ["student", "lesson"]


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


class Comment(models.Model):
    content = models.TextField(verbose_name="Комментарий")
    author = models.ForeignKey("core.User", on_delete=models.CASCADE, verbose_name="Автор", related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания комментария", blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name="Модель")
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field="content_type", fk_field="object_id")
    likes = models.ManyToManyField("core.User")

    def __str__(self):
        return f"{self.content} {self.object_id}"


    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["object_id"]