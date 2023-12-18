from django.urls import path
from . import views

app_name='Main'

urlpatterns = [
    path('', views.home, name='Home')
]
