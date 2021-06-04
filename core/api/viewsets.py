#from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AbrigoSerializer , AnimalSerializer
from core.models import Abrigo, Animal

from rest_framework import filters
from rest_framework.filters import SearchFilter

from core.api import serializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class ListarAbrigoAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    
    serializer_class = AbrigoSerializer
    queryset = Abrigo.objects.all()

class AbrigoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Abrigo.objects.all()
    serializer_class = AbrigoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome'] #filtro de pesquisa

class ListarAnimalAPIView(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get_queryset(self):
        if self.kwargs.get('abrigo_pk'):
            return self.queryset.filter(abrigo_id=self.kwargs.get('abrigo_pk'))
        return self.queryset.all()

class AnimalAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['tipo', 'raca'] #filtro de pesquisa