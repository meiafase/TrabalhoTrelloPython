import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from . models import Tarefas, Usuario

def boardHome(request):
    id_usuario = request.session.get('idUsuario', False)

    if (id_usuario):
        usuario = Usuario.objects.get(idUsuario=id_usuario)
        tarefasUsuario = Tarefas.objects.filter(idUsuario=id_usuario)


        return render(request, 'board/indexBoard.html', {
            'nome': usuario.nome,
            'tarefasUsuario': tarefasUsuario,
            'idUsuario': usuario.idUsuario,
        })
    else:
        return redirect('http://127.0.0.1:8000/')
        

 
def inserirTarefa(request, idUsuario):
    id_usuario = request.session.get('idUsuario', False)

    if (id_usuario):
        usuario = get_object_or_404(Usuario, idUsuario=idUsuario)

        if request.method == "POST":
            titulo = request.POST.get('titulo')
            descricao = request.POST.get('descricao')
            situacao = int(request.POST.get('situacao'))

            tarefa = Tarefas(idUsuario=usuario, titulo=titulo, descricao=descricao, situacao=situacao)
            tarefa.save()

            return redirect('http://127.0.0.1:8000/board')
        
        else:
            return render(request, 'board/inserirTarefa.html', {'idUsuario': idUsuario})
    else:
        return redirect('http://127.0.0.1:8000/')
    
    

def editarTarefa(request, idTarefa):
    id_usuario = request.session.get('idUsuario', False)

    if (id_usuario):
        tarefa = get_object_or_404(Tarefas, idTarefa=idTarefa)

        if request.method == "POST":
            titulo = request.POST.get('titulo', tarefa.titulo)
            descricao = request.POST.get('descricao', tarefa.descricao)
            situacao = int(request.POST.get('situacao', tarefa.situacao))
            
            tarefa.titulo = titulo
            tarefa.descricao = descricao
            tarefa.situacao = situacao
            tarefa.save()

            return redirect('http://127.0.0.1:8000/board')
        
        elif request.method == "PUT": 
            data = json.loads(request.body)
            novo_estado = data.get('newBoardId')
            situacao = 1
            if (novo_estado == 'boardFeito'):
                situacao = 3
            elif (novo_estado == 'boardFazendo'):
                situacao = 2
            elif (novo_estado == "boardAfazer"):
                situacao = 1

            tarefa = Tarefas.objects.get(idTarefa=idTarefa)
            tarefa.situacao = situacao
            tarefa.save()
            
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return render(request, 'board/editarTarefa.html', {'tarefa': tarefa})
    else:
        return redirect('http://127.0.0.1:8000/')


def excluirTarefa(request, idTarefa):
    tarefa = get_object_or_404(Tarefas, idTarefa=idTarefa)

    if request.method == "GET":
        tarefa.delete()

        return redirect('http://127.0.0.1:8000/board')
    

def destruirSessao(request):
    request.session.flush()

    return redirect('http://127.0.0.1:8000/')
    