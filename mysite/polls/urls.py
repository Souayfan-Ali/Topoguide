from django.contrib import admin
from django.urls import path, include

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.Itineraire_list, name='Itineraire_list'),
    path('<int:Itineraire_id>/', views.Itineraire_DetailView, name='Itineraire_DetailView'),
    path('<int:Itineraire_id>/Ajouter_une_Sortie/', views.Ajouter_une_Sortie, name='Ajouter_une_Sortie'),
    path('Consulter/<int:sortie_id>/', views.Consulter, name='Consulter'),
    path('Modifier/<int:sortie_id>/', views.Modifier, name='Modifier'),
    path('accounts/', include('django.contrib.auth.urls'),name='login'),
    path('accounts/', include('django.contrib.auth.urls'),name='logout'),
]