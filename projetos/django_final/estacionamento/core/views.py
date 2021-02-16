from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa, Veiculo, MovRotativoHora

# Create your views here.
def home(request):
    contexto = {'mensagem': 'Ola Mundo'}
    return render(request, 'core/html/index.html', contexto)


def cadastro_pessoas(request):
    contexto = {'titulo_pagina': 'Lista de cadastros', 'pessoas': Pessoa.objects.all()}
    return render(request, 'core/html/lista_pessoas.html', contexto)


def cadastro_veiculos(request):
    contexto = {'titulo_pagina': 'Lista de veiculos', 'veiculos': Veiculo.objects.all()}
    return render(request, 'core/html/lista_veiculos.html', contexto)

def rot_hora(request):
    contexto = {'titulo_pagina': 'Rotação de veiculos por hora', 'rot_hora': MovRotativoHora.objects.all()}
    return render(request, 'core/html/mov_rot_hora.html', contexto)