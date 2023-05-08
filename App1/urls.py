from django.urls import path 
from App1 import views 

urlpatterns=[

    path('', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('contacto', views.contacto, name='Contacto'),
    path('productos', views.productos, name='Productos'),
    path('info', views.info, name='Info'),
    path('busquedaCurso',views.busquedaCurso,name="BusquedaCurso"),
    path('buscar/',views.buscar),
]
