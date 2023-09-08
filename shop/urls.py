from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('about/', views.About.as_view(), name='about'),
    path('service/', views.Service.as_view(), name='services'),
    path('shop/', views.Shop.as_view(), name='shop'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
]