from django.db import models

PAGE_SIZE = 9


class StudentLessonStatus(models.TextChoices):
    NOT_COMPLETED = "not_completed", "Не пройден"
    COMPLETED = "completed", "Пройден"


class DaysOfWeek(models.IntegerChoices):
    MONDAY = 1, "Понедельник"
    TUESDAY = 2, "Вторник"
    WEDNESDAY = 3, "Среда"
    THURSDAY = 4, "Четверг"
    FRIDAY = 5, "Пятница"
    SATURDAY = 6, "Суббота"
    SUNDAY = 7, "Воскресенье"
