from django.urls import path
from .apps import OrganizadorConfig
from django.shortcuts import render
from .views import OrganizadorListView, OrganizadorCreateView, OrganizadorDeleteView, OrganizadorUpdateView


app_name = OrganizadorConfig.nome
urlpatterns = [
    path('', OrganizadorListView.as_view(), name='org_list'),
    path('create/', OrganizadorCreateView.as_view(), name='org_create'),
    path('update/<int:pk>/', OrganizadorUpdateView.as_view(), name='org_update'),
    path('delete/<int:pk>', OrganizadorDeleteView.as_view(), name='org_delete'),
]


