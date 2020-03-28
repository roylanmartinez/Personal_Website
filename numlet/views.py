from django.shortcuts import render
from .numlett import Numero


def numlet(request):
    return render(request, 'numlet/numletES.html')


def calcular(request):
    originaln = request.GET['numero']
    originalf = request.GET['formato']
    if originalf == '1':
        resultadov = Numero(originaln).a_letras.lower()
    elif originalf == '2':
        resultadov = Numero(originaln).a_letras.upper()
    elif originalf == '3':
        resultadov = Numero(originaln).a_letras.capitalize()
    else:
        resultadov = Numero(originaln).a_letras
    context = {'resultadov': resultadov,
               'originaln': originaln, 'originalf': originalf}
    print(context['originaln'], context['originalf'])
    return render(request, 'numlet/numletES.html', context)
