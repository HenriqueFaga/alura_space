from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index),
    path('imagem.html', imagem)
]
