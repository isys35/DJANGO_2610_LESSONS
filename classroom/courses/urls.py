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
    path("roadmaps/", views.RoadMapListView.as_view(), name="roadmap_list"),
    path("roadmaps/create/", views.RoadMapCreateView.as_view(), name="roadmap_create"),
    path("roadmaps/<int:pk>/", views.RoadMapDetailView.as_view(), name="roadmap_detail"),
    path("roadmaps/<int:pk>/update/", views.RoadMapUpdateView.as_view(), name="roadmap_update"),
    path("add_comment_like/<int:pk>/", views.add_comment_like, name="add_comment_like")
]