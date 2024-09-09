import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from . models import Tarefas, Usuario

def boardHome(request):
    return render(request, 'board/indexBoard.html')

 
def inserirTarefa(request, idUsuario):
    usuario = get_object_or_404(Usuario, idUsuario=idUsuario)

    if request.method == "POST":
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        situacao = int(request.POST.get('situacao'))

        tarefa = Tarefas(idUsuario=usuario, titulo=titulo, descricao=descricao, situacao=situacao)
        tarefa.save()

        userContent = Usuario.objects.get(idUsuario=idUsuario)
        tarefasUsuario = Tarefas.objects.filter(idUsuario=usuario)

        return render(request, 'board/indexBoard.html', {
            'nome': userContent.nome, 
            'tarefasUsuario': tarefasUsuario, 
            'idUsuario': usuario.idUsuario
        })
    
    else:
        return render(request, 'board/inserirTarefa.html', {'idUsuario': idUsuario})
    
    

def editarTarefa(request, idTarefa):
    tarefa = get_object_or_404(Tarefas, idTarefa=idTarefa)

    if request.method == "POST":
        titulo = request.POST.get('titulo', tarefa.titulo)
        descricao = request.POST.get('descricao', tarefa.descricao)
        situacao = int(request.POST.get('situacao', tarefa.situacao))
        
        tarefa.titulo = titulo
        tarefa.descricao = descricao
        tarefa.situacao = situacao
        tarefa.save()

        idUsuario = tarefa.idUsuario.idUsuario
        tarefasUsuario = Tarefas.objects.filter(idUsuario=idUsuario)

        
        # return HttpResponse("asdasdasd")
        return render(request, 'board/indexBoard.html', {
            'nome': tarefa.idUsuario.nome, 
            'tarefasUsuario': tarefasUsuario, 
            'idUsuario': idUsuario
        })
    
    elif request.method == "PUT": 
        data = json.loads(request.body)
        novo_estado = data.get('newBoardId')
        situacao = 1
        if (novo_estado == 'boardFeito'):
            situacao = 3
        elif novo_estado == 'boardFazendo':
            situacao = 2
        elif novo_estado == "boardAfazer":
            situacao = 1

        tarefa = Tarefas.objects.get(idTarefa=idTarefa)

        tarefa.situacao = situacao
        tarefa.save()
        
        return JsonResponse({'status': 'success'}, status=200)
    else:
        return render(request, 'board/editarTarefa.html', {'tarefa': tarefa})



def excluirTarefa(request, idTarefa):
    tarefa = get_object_or_404(Tarefas, idTarefa=idTarefa)
    idUsuario = tarefa.idUsuario.idUsuario

    if request.method == "GET":
        tarefa.delete()

        usuario = get_object_or_404(Usuario, idUsuario=idUsuario)
        tarefasUsuario = Tarefas.objects.filter(idUsuario=usuario)

        print (tarefa.idUsuario.nome)
        return render(request, 'board/indexBoard.html', {
            'nome': tarefa.idUsuario.nome, 
            'tarefasUsuario': tarefasUsuario, 
            'idUsuario': idUsuario
        })
    