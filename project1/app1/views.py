from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def money(request):
    return HttpResponse('<h1>I need money</h1>')