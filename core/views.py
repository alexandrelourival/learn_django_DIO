from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} de {idade} anos.</h1>')

def soma(request, a, b):
    return HttpResponse(f'<h1> {a} + {b} = {a+b}</h1>')

def subtracao(request, a, b):
    return HttpResponse(f'<h1> {a} - {b} = {a-b}</h1>')

def multiplicacao(request, a, b):
    return HttpResponse(f'<h1> {a} * {b} = {a*b}</h1>')

def divisao(request, a, b):
    return HttpResponse(f'<h1> {a} / {b} = {a/b}</h1>')
