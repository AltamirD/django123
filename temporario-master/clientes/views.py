from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, logout, login
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('password')
        user = authenticate(username=email, password=senha)

        if user:
            login(request, user)
            return redirect('produtos:principal')
        else:
            messages.info(request, 'OOOOPS! DADOS INVÁLIDOS')

    return render(request, 'clientes/login.html')


def cadastro(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('password')
        usuario_criado = get_user_model().objects.create(email=email)
        usuario_criado.set_password(senha)
        usuario_criado.save()

    return render(request, 'clientes/cadastro.html')


def deslogar(request):
    logout(request)
    return redirect(reverse('produtos:principal'))