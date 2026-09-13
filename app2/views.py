from django.shortcuts import render
from django.http import HttpResponse

def vista_tres(request):
    return HttpResponse("<h1>App 2 - Vista Principal</h1>")

def vista_cuatro(request):
    return HttpResponse("<h1>App 2 - Vista Secundaria</h1>")
# Create your views here.
