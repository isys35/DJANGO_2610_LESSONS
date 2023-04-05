from django.urls import path
from courses import views

app_name = "courses"

urlpatterns = [
    path("", views.CoursesListView.as_view(), name="list"),
    path("create/", views.CourseCreateView.as_view(), name="create"),
    path("<int:pk>/", views.CourseDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", views.CourseUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.CourseDeleteView.as_view(), name="delete"),
    path("<int:pk>/add_comment/", views.add_comment, name="add_comment"),
    path("add_comment_like/<int:pk>/", views.add_comment_like, name="add_comment_like")
]