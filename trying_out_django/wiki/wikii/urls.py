from django.urls import path
from . import views
app_name = "wikii"
urlpatterns = [
    path('', views.home, name= "home"),
    path('new', views.new, name="new"),
    path('<str:title>', views.article, name="article")
]
