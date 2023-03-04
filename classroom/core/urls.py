from django.urls import path
from core import views
from django.contrib.auth import views as auth_views

from user_role.views import LoginView

app_name = "core"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="core/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("users/list/", views.UserListView.as_view(), name="users_list"),
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="users_update"),
    path("users/create/", views.UserCreateView.as_view(), name="users_create"),
    path("users/groups/", views.GroupListView.as_view(), name="group_list"),
    path("users/groups/create/", views.RoleCreateView.as_view(), name="group_create"),

]
