from django.urls import path
from courses import views

app_name = "courses"

urlpatterns = [
    path("", views.CoursesListView.as_view(), name="list"),
    path("create/", views.CreateCourseView.as_view(), name="create"),
    path("<int:pk>/", views.DetailCourseView.as_view(), name="detail"),
    path("<int:pk>/update/", views.UpdateCourseView.as_view(), name="update"),
    path("<int:pk>/delete/", views.DeleteCourseView.as_view(), name="delete"),
    path("roadmaps/", views.RoadMapListView.as_view(), name="roadmap_list"),
    path("roadmaps/create/", views.CreateRoadMapView.as_view(), name="roadmap_create"),
    path("roadmaps/<int:pk>/", views.DetailRoadMapView.as_view(), name="roadmap_detail"),
    path("roadmaps/<int:pk>/update/", views.UpdateRoadMapView.as_view(), name="roadmap_update"),
]
