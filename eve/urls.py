from django.urls import path
from .apps import PeConfig
from .views import EventoListView, EventoCreateView, EventoDeleteView, EventoUpdateView


app_name = PeConfig.name
urlpatterns = [
    path('', EventoListView.as_view(), name='eve_list'),
    path('create/', EventoCreateView.as_view(), name='eve_create'),
    path('update/<int:pk>/', EventoUpdateView.as_view(), name='eve_update'),
    path('delete/<int:pk>', EventoDeleteView.as_view(), name='eve_delete'),
]

