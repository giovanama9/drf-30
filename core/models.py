from django.db import models

class Abrigo(models.Model):
    nome = models.CharField("nome", max_length = 80)
    #cidade = models.CharField("cidade", max_length= 30)
    #estado = models.CharField("estado", max_length= 30)
    logradouro = models.CharField("logradouro", max_length = 80)
    bairro = models.CharField("bairro", max_length = 80)
    numero = models.IntegerField("numero")
    telefone = models.CharField("telefone", max_length= 13)
    cnpj = models.CharField("cnpj", max_length=13, unique=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table= 'abrigo'
        verbose_name = "Abrigo" 
        verbose_name_plural = "Abrigos"

class Animal(models.Model):
    
    nomeAnimal = models.CharField("nome do Pet", max_length=50)
    situacao = models.CharField("situação", max_length= 100)
    raca = models.CharField("raça", max_length=50, null=True, blank=True)
    tipo = models.CharField("tipo de pet", max_length=50)
    descricao = models.CharField("descrição do pet", max_length=50)
    begin_date= models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)#para verificar se o pet está disponivel para doação

    disponivel = models.BooleanField("Pet disponivel", default=False)
    
    abrigo = models.ForeignKey(Abrigo,on_delete=models.CASCADE,related_name='animal_abrigo',verbose_name='Abrigo')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table= 'animal'
        verbose_name= "Animal"
        verbose_name_plural= "Animais"

# Create your models here.
