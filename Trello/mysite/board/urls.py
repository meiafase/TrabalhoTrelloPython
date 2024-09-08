from django.urls import path
from . import views

urlpatterns = [
    path('', views.boardHome, name="boardHome"),
    path('teste/', views.boardHome, name="boardHome"),
    path('inserirTarefa/<int:idUsuario>/', views.inserirTarefa, name="inserirTarefa"),
    path('editarTarefa/<int:idTarefa>/', views.editarTarefa, name="editarTarefa"),
]
