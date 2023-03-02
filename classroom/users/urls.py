from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("", views.ListUsersView.as_view(), name="list"),
    path("create/", views.CreateUserView.as_view(), name="create"),
    path("groups/", views.ListGroupsView.as_view(), name="group_list"),
    path("groups/create", views.CreateGroupView.as_view(), name="group_create"),
]