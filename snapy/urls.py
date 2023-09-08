from django.urls import path

from . import views

urlpatterns = [
    path('', views.Snapy.as_view(), name='snapy'),
    path('gallery/<int:pk>', views.Gallery.as_view(), name='gallery'),
    path('add/', views.Add.as_view(), name='add'),
]