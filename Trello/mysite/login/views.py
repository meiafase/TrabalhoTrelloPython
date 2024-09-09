from django.shortcuts import render

from board.models import Usuario, Tarefas


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        logar = Usuario.objects.filter(email=email, senha=senha)
        if logar:
            tarefasUsuario = Tarefas.objects.filter(idUsuario=logar[0].idUsuario)
            return render(request, 'board/indexBoard.html', {'nome': logar[0].nome, 'tarefasUsuario': tarefasUsuario, 'idUsuario': logar[0].idUsuario})
        else:
            return render(request, 'login/login.html')
    else:
        return render(request, 'login/login.html')
