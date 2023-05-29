from django.urls import path 
from App1 import views 
from django.contrib.auth.views import LogoutView

urlpatterns=[

    path('', views.inicio, name="Inicio"),
    path('contacto', views.contacto, name='Contacto'),
    path('libros', views.libros, name='Libros'),
    path('formularioLibro', views.formularioLibro, name='FormularioLibro'),
    path('about', views.about, name='About'),
    path('info', views.info, name='Info'),
    path('login',views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='App1/logout.html'), name='Logout'),
    path('leerLibros', views.leerLibros, name='LeerLibros'),
    
    
]
