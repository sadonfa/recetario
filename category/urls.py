from django.urls import path
# from rest_framework import 
from .views import Category, CategoryParametros

urlpatterns = [
    path('categoria/', Category.as_view()),
    path('categoria/<int:id>/', CategoryParametros.as_view()),
]
