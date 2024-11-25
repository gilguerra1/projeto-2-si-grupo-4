from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from users.models import User
import logging

logger = logging.getLogger(__name__)

@login_required
def home_view(request):
    return render(request, 'Home.html')

def how_it_works_view(request):
    return render(request, 'Como_Funciona.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        logger.debug(f"Tentando autenticar o usuário: {email}")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            logger.debug(f"Usuário autenticado: {user.email}, Role: {user.role}")

            login(request, user)
            messages.success(request, "Login realizado com sucesso!")

            if user.role == 'Professor':
                logger.debug("Redirecionando para questionário.")
                return redirect('questionario')  
            elif user.role == 'Student':
                logger.debug("Redirecionando para home do usuário.")
                return redirect('home-usuario')  
            else:
                logger.error("Role desconhecido!")
                messages.error(request, "Papel desconhecido para o usuário.")
        else:
            logger.error(f"Autenticação falhou para o usuário: {email}")
            messages.error(request, "Credenciais inválidas.")

    return render(request, 'Login.html')

def user_register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        register = request.POST.get('register')

        if not all([name, email, password, confirm_password, register]):
            messages.error(request, 'Todos os campos são obrigatórios!')
            return render(request, 'Cadastro.html')

        if password != confirm_password:
            messages.error(request, 'As senhas não coincidem!')
            return render(request, 'Cadastro.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Esse e-mail já está cadastrado.')
            return render(request, 'Cadastro.html')

        if User.objects.filter(register=register).exists():
            messages.error(request, 'Essa matrícula já está cadastrada.')
            return render(request, 'Cadastro.html')

        try:
            user = User(
                name=name,
                email=email,
                password=make_password(password),  
                register=register
            )
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso.')
            return redirect('/admin/')  
        except Exception as e:
            logger.error(f"Erro ao criar usuário: {e}")
            messages.error(request, f'Erro ao criar usuário: {e}')
            return render(request, 'Cadastro.html')

    return render(request, 'Cadastro.html')
