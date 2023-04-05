from django.db import models


class QuerySetCountStudent(models.QuerySet):

    def with_count_students(self):
        return self.annotate(count_students=models.Count("students"))

    def _some_method(self):
        print("Приватный метод")
        return self

    def _some_method2(self):
        print("Приватный метод 2")
        return self

    _some_method2.queryset_only = False

    def some_method3(self):
        print("Публичный метод")
        return self

    some_method3.queryset_only = True


class PublicatedManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(publicated=True)

    def get_related(self):
        return self.get_queryset().select_related("author").prefetch_related("students")
