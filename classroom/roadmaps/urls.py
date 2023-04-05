from django.urls import path
from roadmaps import views

urlpatterns = [
    path("", views.RoadMapListView.as_view(), name="list"),
    path("create/", views.RoadMapCreateView.as_view(), name="create"),
    path("<int:pk>/", views.RoadMapDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", views.RoadMapUpdateView.as_view(), name="update"),
]