from django.db import models

PAGE_SIZE = 9


class StudentLessonStatus(models.TextChoices):
    NOT_COMPLETED = "not_completed", "Не пройден"
    COMPLETED = "completed", "Пройден"


class DaysOfWeek(models.IntegerChoices):
    MONDAY = 0, "Понедельник"
    TUESDAY = 1, "Вторник"
    WEDNESDAY = 2, "Среда"
    THURSDAY = 3, "Четверг"
    FRIDAY = 4, "Пятница"
    SATURDAY = 5, "Суббота"
    SUNDAY = 6, "Воскресенье"
