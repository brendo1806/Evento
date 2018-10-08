from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Eve
from django.urls import reverse_lazy

class EventoListView(ListView):
    model = Eve


class EventoCreateView(CreateView):
    model = Eve
    fields = {'nome', 'descricao'}
    success_url = reverse_lazy('eve_list')


class EventoUpdateView(UpdateView):
    model = Eve
    fields = ['nome', 'descricao']
    success_url = reverse_lazy('eve_list')


class EventoDeleteView(DeleteView):
    model = Eve
    success_url = reverse_lazy('eve_list')

def index(request):
    render(request, 'index.html')
