from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos
# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "direccion", "email", "telefono")
    search_fields = ("nombre", "direccion", "email", "telefono")
    list_per_page = 7
    

class ArticulosAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "seccion", "precio")
    search_fields = ("nombre", "seccion", "precio")
    list_per_page = 7
    list_filter = ("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    list_display = ("id", "numero", "fecha", "entregado")
    search_fields = ("numero", "fecha", "entregado")
    list_per_page = 7
    list_filter = ("fecha",)
    date_hierarchy = "fecha"


admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)