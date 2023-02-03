from django.urls import path

from homeworks.views import index

urlpatterns = [
    path("", index)
]
