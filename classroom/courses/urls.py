from django.urls import path
from courses import views

app_name = "courses"

urlpatterns = [
    path("", views.courses_list, name="list"),
    path("create/", views.course_create, name="create"),
]