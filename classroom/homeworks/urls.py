from django.urls import path

from homeworks.views import index

app_name = "homeworks"

urlpatterns = [
    path("", index, name="list")
]
