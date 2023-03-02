from django.urls import path
from django.contrib.auth import views as auth_views

app_name = "core"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="auth/login.html"), name="login"),
    path("login/", auth_views.LogoutView.as_view(), name="logout"),
]