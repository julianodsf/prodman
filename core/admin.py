from django.contrib import admin
from .models import *

class ItemReceitaInline(admin.TabularInline):
    model = ItemReceita
    extra = 1

class ReceitaAdmin(admin.ModelAdmin):
    inlines = [ItemReceitaInline]

class ItemCompraInline(admin.TabularInline):
    model = ItemCompra
    extra = 1

class CompraAdmin(admin.ModelAdmin):
    inlines = [ItemCompraInline]

admin.site.register(Insumo)
admin.site.register(Produto)
admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Compra, CompraAdmin)