from django.urls import path
from . import views

urlpatterns = [
    path('', views.boardHome, name="boardHome"),
    path('inserirTarefa/<int:idUsuario>/', views.inserirTarefa, name="inserirTarefa"),
    path('editarTarefa/<int:idTarefa>/', views.editarTarefa, name="editarTarefa"),
    path('excluirTarefa/<int:idTarefa>/', views.excluirTarefa, name="excluirTarefa"),
    path('destruirSessao/', views.destruirSessao, name="destruirSessao"),
]
