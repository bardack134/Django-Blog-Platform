from django.shortcuts import render, redirect

from .models import post
# Create your views here.

def home(request):
    datos = post.objects.all()
    
    context = {
        'datos': datos
    }
    
    return render(request, 'cards.html', context)


def blog(request, blog_id):
    # Con el id usando el metodo  get(. recordando que el metodo get() en un modelo de Django se utiliza para recuperar un único objeto que cumple con los criterios de búsqueda especificados. 
    dato=post.objects.get(id=blog_id)
       
    
    context = {
        'dato_post': dato
    }
    
    # renderizamos el item especifico obtenido a nuestra plantilla
    return render(request, 'post.html', context)