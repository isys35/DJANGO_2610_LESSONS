from django.urls import path
from courses import views

app_name = "courses"

urlpatterns = [
    path("", views.CoursesListView.as_view(), name="list"),
    path("create/", views.CourseCreateView.as_view(), name="create"),
    path("<int:id>/", views.course_detail, name="detail"),
    path("<int:id>/update/", views.course_update, name="update"),
    path("<int:id>/delete/", views.course_delete, name="delete"),
]
