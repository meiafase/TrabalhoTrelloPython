from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from board.models import Usuario

def cadastro(request):
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmarSenha')

        print(usuario, email, senha, confirmar_senha)

        if Usuario.objects.filter(nome=usuario).exists():
            messages.error(request, 'O nome de usuário já está em uso.')
            return render(request, 'cadastro/IndexCadastro.html')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'O e-mail já está em uso.')
            return render(request, 'cadastro/IndexCadastro.html')

        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'cadastro/IndexCadastro.html')

        Usuario.objects.create(nome=usuario, email=email, senha=senha)
        messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
        return redirect("../")

    else:
        return render(request, 'cadastro/IndexCadastro.html')