from django.urls import path

from . import views

urlpatterns = [
    path('expense-tracker/', views.Money.as_view(), name='money'),
]