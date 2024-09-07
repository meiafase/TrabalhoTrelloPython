from django.urls import path
from . import views

urlpatterns = [
    path('', views.boardHome, name="boardHome"),
    path('inserirTarefa/', views.inserirTarefa, name="inserirTarefa"),
    path('editarTarefa/<int:id>/', views.editarTarefa, name="editarTarefa"),
]
