from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from . models import Tarefas, Usuario

def boardHome(request):
    return render(request, 'board/indexBoard.html')

 
def inserirTarefa(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        situacao = int(request.POST.get('situacao'))
        usuario = Usuario.objects.get(idUsuario=1)
        tarefa = Tarefas(idUsuario=usuario, titulo=titulo, descricao=descricao, situacao=situacao)
        tarefa.save()

        # tarefasUsuario = Tarefas.objects.filter(idUsuario=logar[0].idUsuario)

        return redirect('../')
    else:
        return render(request, 'board/inserirTarefa.html')


def editarTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, id=id)
    return render(request, 'board/editarTarefa.html')