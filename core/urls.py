from django.urls import path

from .views import (calendario, cliente, clientes, contato, curso, cursos,
                    index, perfil)

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('curso/<int:id>', curso, name='curso'),
    path('cliente/<int:id>', cliente, name='cliente'),
    path('cursos', cursos, name='cursos'),
    path('clientes', clientes, name='clientes'),
    path('calendario', calendario, name='calendario'),
    path('perfil', perfil, name='perfil'),
]
