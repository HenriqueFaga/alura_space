from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "categoria", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome", "id", "legenda")
    list_editable = ("publicada",)
    list_filter = ("categoria", "usuario",)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)
