from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm


def novo_usuario(request):
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get('username')
            messages.success(
                request, f'O usuário {usuario} foi criado com sucesso!')
            return redirect('clientes')

    else:
        formulario = UserRegisterForm()

    return render(request, 'usuarios/novo_usuario.html', {'formulario': formulario})
