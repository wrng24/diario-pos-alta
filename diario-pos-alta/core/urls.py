from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pacientes/', views.listar_pacientes, name='pacientes'),
    path('pacientes/cadastrar/', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('pacientes/<int:paciente_id>/', views.detalhe_paciente, name='detalhe_paciente'),
    path('pacientes/<int:paciente_id>/registro/cadastrar/', views.cadastrar_registro, name='cadastrar_registro'),
    path('registros/<int:registro_id>/', views.detalhe_registro, name='detalhe_registro'),
    path('pacientes/<int:paciente_id>/editar/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/<int:paciente_id>/excluir/', views.excluir_paciente, name='excluir_paciente'),
    path('registros/<int:registro_id>/editar/', views.editar_registro, name='editar_registro'),
    path('registros/<int:registro_id>/excluir/', views.excluir_registro, name='excluir_registro'),
    path('login/', views.login_usuario, name='login'),
path('logout/', views.logout_usuario, name='logout'),
]
