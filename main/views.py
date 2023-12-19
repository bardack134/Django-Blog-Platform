from django.shortcuts import render, redirect

from .models import post
# Create your views here.

def home(request):
    datos = post.objects.all()
    
    context = {
        datos: datos
    }
    
    return render(request, 'cards.html', context)