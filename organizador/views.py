from django.shortcuts import render
from .models import Organizador
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class OrganizadorCreateView(CreateView):
    model = Organizador
    fields = {'nome', 'descricao'}
    success_url = reverse_lazy('org_list')

class OrganizadorListView(ListView):
    model = Organizador
    fields = {'nome', 'descricao'}

class OrganizadorUpdateView(UpdateView):
    model = Organizador
    success_url = reverse_lazy('org_list')

class OrganizadorDeleteView(DeleteView):
    model = Organizador
    success_url = reverse_lazy('org_list')
