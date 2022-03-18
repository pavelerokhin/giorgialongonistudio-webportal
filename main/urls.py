from django.urls import path

from main import views

urlpatterns = [
    path('', views.index),
    path('projects/<str:type>', views.projects),
    path('detail/<str:id>', views.project_detail),
]
