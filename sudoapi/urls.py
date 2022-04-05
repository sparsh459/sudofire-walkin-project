from django.urls import path, include
from sudoapi import views

urlpatterns = [
    path('user/', views.create_user),
    path('customer/', views.create_customer),
]
