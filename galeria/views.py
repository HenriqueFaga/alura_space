from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia
from django.contrib import messages

def index(request):
    # request, template_name, context=None, content_type=None, status=None, using=None
    if not request.user.is_authenticated:
        messages.error(request, "Usuario não logado!")
        return redirect('login')

    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', context={'cards': fotografias})

def imagem(request, foto_id):
    if not request.user.is_authenticated:
        messages.error(request, "Usuario não logado!")
        return redirect('login')

    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuario não logado!")
        return redirect('login')

    if "buscar" in request.GET and request.GET['buscar']:
        fotografias = Fotografia.objects.filter(nome__icontains=request.GET['buscar'], publicada=True).order_by("-data_fotografia")
    else:
        fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, "galeria/buscar.html", context={'cards': fotografias})
