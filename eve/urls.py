from django.urls import path
from .views import EventoListView, EventoCreateView, EventoDeleteView, EventoUpdateView
urlpatterns = [
    path('', EventoListView.as_view(), name='eve_list'),
    path('create/', EventoCreateView.as_view(), name='eve_create'),
    path('update/<pk::int>', EventoUpdateView.as_view(), name='eve_update'),
    path('delete/<pk::int>', EventoDeleteView.as_view(), name='eve_delete'),
]

