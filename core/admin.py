from django.contrib import admin
from .models import Abrigo
from .models import Animal

@admin.register(Abrigo)
class AbrigoAdmin(admin.ModelAdmin):
    list_display = ['id','nome','bairro','telefone','cnpj']

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['nomeAnimal','abrigo','tipo','descricao','disponivel']
# Register your models here.
