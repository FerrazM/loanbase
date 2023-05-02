from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import date


@login_required
def clientes(request):
    hoje = date.today()
    dados_cliente = {
        'dados': Cliente.objects.filter(usuario=request.user).exclude(checkbox2=True),
        'hoje': hoje
    }
    return render(request, 'loans/clientes.html', dados_cliente)


@login_required
def detalhe(request, id_cliente):
    cliente = Cliente.objects.get(pk=id_cliente)
    valor_retornado = cliente.juros_mes * cliente.parcelas_pagas
    dados = {
        'dados': cliente,
        'valor_retornado': valor_retornado
    }
    return render(request, 'loans/detalhe.html', dados)


@login_required
def criar(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente = cliente_form.save(commit=False)
            cliente.usuario = request.user
            cliente.save()
        return redirect('clientes')
    else:
        cliente_form = ClienteForm()
        formulario = {
            'formulario': cliente_form
        }
        return render(request, 'loans/novo_emprestimo.html', context=formulario)


@login_required
def editar(request, id_cliente):
    cliente = Cliente.objects.get(pk=id_cliente)
    if request.method == 'GET':
        formulario = ClienteForm(instance=cliente)
        return render(request, 'loans/novo_emprestimo.html', {'formulario': formulario})
    else:
        formulario = ClienteForm(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
        return redirect('clientes')


@login_required
def excluir(request, id_cliente):
    cliente = Cliente.objects.get(pk=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')
    return render(request, 'loans/confirmar_exclusao.html', {'item': cliente})


@login_required
def somaemprestimos(request):
    soma_valor = Cliente.objects.filter(
        usuario=request.user).aggregate(Sum('valor'))
    soma_pagamento = Cliente.objects.filter(
        usuario=request.user).aggregate(Sum('juros_mes'))
    context = {'soma_valor': soma_valor, 'soma_pagamento': soma_pagamento}
    return render(request, 'loans/balanco.html', context)


@login_required
def balancomensal(request):
    if request.method == 'POST':
        inicio_mes = request.POST.get('inicio')
        fim_mes = request.POST.get('fim')
        soma_valor = Cliente.objects.filter(usuario=request.user, data_emprestimo__range=[
                                            inicio_mes, fim_mes]).aggregate(Sum('valor'))
        soma_pagamento = Cliente.objects.filter(usuario=request.user, vencimento_mensal__range=[
                                                inicio_mes, fim_mes]).aggregate(Sum('juros_mes'))
        return render(request, 'loans/balanco_mensal.html/', {
            'soma_valor': soma_valor['valor__sum'],
            'soma_pagamento': soma_pagamento['juros_mes__sum']
        })
    else:
        return render(request, 'loans/balanco_mensal.html')


@login_required
def pagos(request):
    dados_cliente = {
        'dados': Cliente.objects.filter(usuario=request.user)
    }
    return render(request, 'loans/divida_paga.html', dados_cliente)
