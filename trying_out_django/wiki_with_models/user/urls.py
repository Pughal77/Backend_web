from os import name
from django.urls import path
from . import views
app_name = "user"
urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('login', views.login_user, name="login"),
    path('logged_out/', views.logout_user, name="logout"),
    path('new_user/', views.create_use, name="create_user")
    ]