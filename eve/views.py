from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Eve

class EventoListView(ListView):
    model = Eve


class EventoCreateView(CreateView):
    model = Eve


class EventoUpdateView(UpdateView):
    model = Eve


class EventoDeleteView(DeleteView):
    model = Eve