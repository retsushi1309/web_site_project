# config/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def worry(request):
    return render(request, 'worry.html')

def flow(request):
    return render(request, 'flow.html')

def about(request):
    return render(request, 'about.html')

def privacy(request):
    return render(request, 'privacy.html')

