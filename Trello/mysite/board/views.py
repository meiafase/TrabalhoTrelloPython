from django.http import HttpResponse
from django.shortcuts import render


def boardHome(request):
    return render(request, 'board/indexBoard.html')


def inserirTarefa(request):
    return render(request, 'board/inserirTarefa.html')


def editarTarefa(request):
    return render(request, 'board/editarTarefa.html')