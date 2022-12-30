from django.urls import path
from rest_framework.authtoken import views as auth_view

from . import views

urlpatterns = [
    path("users/", views.UserView.as_view(), name="register"),
    path("users/<str:id>", views.UserDetailView.as_view(), name="detail"),
    path("login/", auth_view.obtain_auth_token, name="login"),
]
