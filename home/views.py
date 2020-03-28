from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import Contactf, Contactfes
from .utils import send_html_mail


def home(request):
    if request.method == 'POST':
        form = Contactf(request.POST or None)
        if form.is_valid():
            form.save()
            namef = str(request.POST['name']).strip().split(' ')
            namef = [word.capitalize() for word in namef]
            emailf = str(request.POST['email'])
            nametf = f'{namef[0]} {namef[1]}' if len(
                namef) > 1 else namef[0]
            send_html_mail(
                f'Hi {nametf}', f"""
                <!DOCTYPE html>
                <html lang="en">
                <body style="text-align: justify; color:black">
                    <div style="padding: 15px">
                        <h1 style="color: rgb(31, 31, 31);">Hey {nametf}!</h1>
                        <hr>
                        <p>Before anything else {namef[0]}, I just want to thank you
                            the time you took to contact me. <br>
                            {namef[0]} I will try to answer you in less than two days,
                            until then, stay safe and have a good day!</p>
                        <p>Kind regards, </p>
                        <div>
                            <h5>Roylan Martínez<br>(Python Hobbyist Developer)</h5>
                        </div>
                        <small style="color:rgb(88, 88, 88)">This is an automatic message, therefore, it is not neccesary to reply
                            it.</small>
                        <br>
                        <small style="color:rgb(88, 88, 88);">If you received this message by error, please send it to spam.</small>
                    </div>
                    <footer style="margin: 15px; text-align:center; border-style: dotted;border-radius: 50px 20px;">
                        <div style="padding: 10px;">
                            <a style="color: rgb(20, 20, 20)" href="https://github.com/roylanmartinez"><b style="font-size:20px"> Github
                                    Profile</b></a>
                        </div>
                    </footer>
                </body>
                </html>
                """, [emailf, ], 'roylanmartinez972@gmail.com')
            messages.success(request, nametf)
            return redirect('pag-en')
        else:
            messages.info(request, '')
            return redirect('pag-en')

    else:
        context = {'form': Contactf()}
        return render(request, 'home/home.html', context)


def homees(request):
    if request.method == 'POST':
        form = Contactf(request.POST or None)
        if form.is_valid():
            form.save()
            namef = str(request.POST['name']).strip().split(' ')
            namef = [word.capitalize() for word in namef]
            emailf = str(request.POST['email'])
            nametf = f'{namef[0]} {namef[1]}' if len(
                namef) > 1 else namef[0]
            send_html_mail(
                f'Hi {nametf}', f"""
                <!DOCTYPE html>
                <html lang="en">
                <body style="text-align: justify; color:black">
                    <div style="padding: 15px">
                        <h1 style="color: rgb(31, 31, 31);">¡Hey {nametf}!</h1>
                        <hr>
                        <p>Antes que nada {namef[0]}, solo quiero agradecerle
                            el tiempo que se tomó en contactarme. <br>
                            {namef[0]} trataré de responderle en menos de dos días.
                            Mientras tanto nnn, cuídese y tenga un buen día!</p>
                        <p>Saludos, </p>
                        <div>
                            <h5>Roylan Martínez<br>(Desarrollador Aficionado de Python)</h5>
                        </div>
                        <small style="color:rgb(88, 88, 88)">Este es un mensaje automático, por lo tanto, no es necesario
                            responder.</small>
                        <br>
                        <small style="color:rgb(88, 88, 88);">Si recibió este mensaje por error, por favor envíelo a spam.</small>

                    </div>
                    <footer style="margin: 15px; text-align:center; border-style: dotted;border-radius: 50px 20px;">
                        <div style="padding: 10px;">
                            <a style="color: rgb(20, 20, 20)" href="https://github.com/roylanmartinez"><b style="font-size:20px">Perfil
                                    de Github</b></a>
                        </div>
                    </footer>
                </body>
                </html>
                """, [emailf, ], 'roylanmartinez972@gmail.com')
            messages.success(request, nametf)
            return redirect('pag-es')
        else:
            messages.info(request, '')
            return redirect('pag-es')

    else:
        context = {'form': Contactf()}
        return render(request, 'home/home.html', context)
