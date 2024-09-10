from django.shortcuts import redirect, render, redirect

from board.models import Usuario

def cadastro(request):
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if Usuario.objects.filter(nome=usuario).exists():
            return render(request, 'cadastro/cadastro.html')

        if Usuario.objects.filter(email=email).exists():
            return render(request, 'cadastro/IndexCadastro.html')
        
        Usuario.objects.create_user(username=usuario, email=email, password=senha)
        return redirect('login')  

        
    else:
        return render(request, 'cadastro/cadastro.html')
