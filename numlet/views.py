from django.shortcuts import render

# Create your views here.


def numlet(request):
    return render(request, 'numlet/numletES.html')
