from django.shortcuts import render
from django.http import HttpResponse

def vista_uno(request):
    return HttpResponse("<h1>App 1 - Vista Principal</h1>")

def vista_dos(request):
    return HttpResponse("<h1>App 1 - Vista Secundaria</h1>")

# Create your views here.
