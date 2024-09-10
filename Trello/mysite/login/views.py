from django.shortcuts import redirect, render
from board.models import Usuario


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            usuario = Usuario.objects.get(email=email, senha=senha)
        except Usuario.DoesNotExist:
            return render(request, 'login/login.html')

        request.session['idUsuario'] = usuario.idUsuario

        return redirect('http://127.0.0.1:8000/board/')

    else:
        id_usuario = request.session.get('idUsuario', False)

        if (id_usuario):
            return redirect('http://127.0.0.1:8000/board/')
        else:
            return render(request, 'login/login.html')