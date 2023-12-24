from django.urls import path
from . import views

app_name='Main'

urlpatterns = [
    path('', views.home, name='Home'),
    # URL DE BLOG, RECIBE COMO PARAMETRO EL ID DEL POST QUE DESEAMOS VER
    path('blog/<int:blog_id>/', views.blog, name='Blog')

]
