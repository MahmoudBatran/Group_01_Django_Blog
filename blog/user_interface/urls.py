from django.urls import path
from .views import login_view, register, logoutUser, block_user

urlpatterns = [
    path("register", register, name="register"),
    path("login", login_view, name="login"),
    path("logout", logoutUser, name="logout"),
    path("block", block_user, name="block_user"),
]