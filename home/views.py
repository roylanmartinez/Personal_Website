from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import Contactf, Contactfes

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = Contactf(request.POST or None)
        if form.is_valid():
            form.save()
            messages.info(request, 'lol', extra_tags='green')
            return redirect('pag-en')
        else:
            messages.info(request, 'lol', extra_tags='red')
            return redirect('pag-en')

    else:
        context = {'form': Contactf()}
        return render(request, 'home/home.html', context)


def homees(request):
    if request.method == 'POST':
        form = Contactfes(request.POST or None)
        if form.is_valid():
            form.save()
            messages.info(request, 'lol', extra_tags='green')
            return redirect('pag-es')
        else:
            messages.info(request, 'lol', extra_tags='red')
            return redirect('pag-es')

    else:
        context = {'form': Contactfes()}
        return render(request, 'home/homeES.html', context)
