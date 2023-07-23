from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path("login/", views.user_login, name='login'),
    path("register/", views.register, name='register'),
    path("logout/", views.user_logout, name='logout'),
    path("profile/", views.user_profile, name='profile'),
]
