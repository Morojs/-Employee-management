from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'admin/index.html')


def navbar(request):
    return render(request, 'admin/menu/navbar.html')


def admin(request):
    return render(request, 'admin/start.html')
