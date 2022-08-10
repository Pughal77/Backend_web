from django.urls import path
from . import views
app_name = "wikii"
urlpatterns = [
    path('home/', views.home, name= "home"),
    path('new/', views.new, name="new"),
    path('<int:id>', views.article, name="article"),
    path('edit/', views.edit, name="edit")
]
