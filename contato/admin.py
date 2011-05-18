from django.contrib import admin
from models import Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome','email','telefone','data_criacao',)
    date_hierarchy = 'data_criacao'
    search_fields = ('nome', 'cpf', 'email',)
    list_filter = ['data_criacao']

admin.site.register(Contato, ContatoAdmin)
