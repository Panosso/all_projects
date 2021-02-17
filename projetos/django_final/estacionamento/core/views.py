from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa, Veiculo, MovRotativoHora, MovRotativoMes
from .forms import PessoaForm, VeiculoForm, MovRotHoraForm, MovRotMesForm

# Create your views here.
def home(request):
    contexto = {'mensagem': 'Ola Mundo'}
    return render(request, 'core/html/index.html', contexto)


def cadastro_pessoas(request):
    form = PessoaForm()
    contexto = {'titulo_pagina': 'Lista de cadastros', 'pessoas': Pessoa.objects.all(), 'form': form}
    return render(request, 'core/html/lista_pessoas.html', contexto)

def cadastro_pessoa(request, id_cadastro):
    data = {}

    #Vai pegar o id da pessoa que vai atualizada
    pessoa = Pessoa.objects.get(id=id_cadastro)

    #Instancia o form, porém com a instancia de pessoa, para carregar no form
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form


    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('pessoas')
    else:
        return render(request, 'core/html/update_pessoa.html', data)


def cadastro_veiculos(request):
    #Pegamos a estrutura que criamos em form.py e passamos para o html
    form = VeiculoForm()
    contexto = {'titulo_pagina': 'Lista de veiculos', 'veiculos': Veiculo.objects.all(), 'form': form}
    return render(request, 'core/html/lista_veiculos.html', contexto)

def rot_hora(request):
    form = MovRotHoraForm()
    contexto = {'titulo_pagina': 'Rotação de veiculos por hora',
                'rot_hora': MovRotativoHora.objects.all(),
                'form': form}
    return render(request, 'core/html/mov_rot_hora.html', contexto)

def rot_mes(request):
    form = MovRotMesForm()
    contexto = {'titulo_pagina': 'Rotação de veiculos por mes',
                'rot_mes': MovRotativoMes.objects.all(),
                'form': form}

    return render(request, 'core/html/mov_rot_mes.html', contexto)

#Recebemos o valor do form e então salvamos caso ele seja valido.
def cadastro_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('pessoas')

def novo_veiculo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('veiculos')

def mov_rot_hora(request):
    form = MovRotHoraForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('rotativos_hora')

def mov_rot_mes(request):
    form = MovRotMesForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('rotativos_mes')
