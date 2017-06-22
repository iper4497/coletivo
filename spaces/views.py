from django.shortcuts import render
#from .models import Space, Tag


def dashboard(request):
    return render(request, 'pruebas.html')

#class