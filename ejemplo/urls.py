from django.urls import path
# from rest_framework import 
from .views import ClassEjemplo, ClassEjemploParametros, ClassEjemploUpload

urlpatterns = [
    path('ejemplo/', ClassEjemplo.as_view()),
    path('ejemplo/<int:id>/', ClassEjemploParametros.as_view() ),
     path('ejemplo-upload/', ClassEjemploUpload.as_view() ),
]
