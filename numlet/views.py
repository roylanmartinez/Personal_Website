from django.shortcuts import render
from .numlett import Numero

# Create your views here.


def numlet(request):
    return render(request, 'numlet/numletES.html')


def calcular(request):
    numerop = request.GET['numero']
    formatop = request.GET['formato']
    context = {'numerop': Numero(numerop).a_letras}
    return render(request, 'numlet/numletES.html', context)
