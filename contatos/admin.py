from django.contrib import admin
from .models import Categoria, Contato
# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'phone', 'email', 
                    'creation_date', 'categoria', 'mostrar')
    list_display_links = ('id', 'name', 'last_name')
    #list_filter = ('name', 'last_name') 
    list_per_page = 10
    search_fields = ('name', 'last_name', 'phone')
    list_editable = ('phone', 'mostrar')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)