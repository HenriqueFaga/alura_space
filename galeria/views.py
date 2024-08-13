from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    # request, template_name, context=None, content_type=None, status=None, using=None
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', context={'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    if "buscar" in request.GET and request.GET['buscar']:
        fotografias = Fotografia.objects.filter(nome__icontains=request.GET['buscar'], publicada=True).order_by("-data_fotografia")
    else:
        fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, "galeria/buscar.html", context={'cards': fotografias})
