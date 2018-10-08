from django.shortcuts import render
from .models import Organizador
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class OrganizadorCreateView(CreateView):
    model = Organizador
    fields = {'nome', 'descricao'}

class OrganizadorListView(ListView):
    model = Organizador
    fields = {'nome', 'descricao'}

class OrganizadorUpdateView(UpdateView):
    model = Organizador

class OrganizadorDeleteView(DeleteView):
    model = Organizador
