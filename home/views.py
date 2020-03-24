from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import Contactf, Contactfes
from .ms import go


def home(request):
    if request.method == 'POST':
        form = Contactf(request.POST or None)
        if form.is_valid():
            nemail = str(request.POST['email'])
            nname = str(request.POST['name']).split(' ')
            nm = ' '.join([word.capitalize() for word in nname])
            form.save()
            go(nombre=nm, correo=nemail)
            messages.success(request, nm)
            return redirect('pag-en')
        else:
            messages.info(request, '')
            return redirect('pag-en')

    else:
        context = {'form': Contactf()}
        return render(request, 'home/home.html', context)


def homees(request):
    if request.method == 'POST':
        form = Contactfes(request.POST or None)
        if form.is_valid():
            nemail = str(request.POST['email'])
            nname = str(request.POST['name']).split(' ')
            nm = ' '.join([word.capitalize() for word in nname])
            form.save()
            go(nombre=nm, correo=nemail)
            messages.success(request, nm)
            return redirect('pag-es')
        else:
            messages.info(request, '')
            return redirect('pag-es')

    else:
        context = {'form': Contactfes()}
        return render(request, 'home/homeES.html', context)
