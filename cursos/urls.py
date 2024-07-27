from django.urls import path
from cursos import views

urlpatterns = [
    path('', views.inicio),
    path('add-profesor/', views.add_profesor, name='add_profesor'),
    path('add-curso/', views.add_curso, name='add_curso'),
    path('add-alumno/', views.add_alumno, name='add_alumno'),
    path('buscar/', views.buscar, name='buscar'),
]
