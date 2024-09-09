
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from Trello.mysite.board.models import Usuario


def cadastro_usuario(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Verifica se o email já esta cadastrado
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "Esse email já está cadastrado.")
            return render(request, 'login/cadastro.html')
        
        # Cria um novo usuário
        novo_usuario = Usuario(nome=nome, email=email, senha=senha)
        novo_usuario.save()
        
        messages.success(request, "Usuário cadastrado com sucesso. Faça login.")
        return redirect('login/login.html')  
    else:
        return render(request, 'login/cadastro.html')
