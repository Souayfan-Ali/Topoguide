from django.contrib import admin
from django.urls import path, include

from . import views
app_name = 'itineraires'
urlpatterns = [
    path('', views.Itineraire_list, name='Itineraire_list'),
    path('<int:itineraire_id>/', views.Itineraire_DetailView, name='Itineraire_DetailView'),
    path('<int:itineraire_id>/Ajouter_une_Sortie/', views.Ajouter_une_Sortie, name='Ajouter_une_Sortie'),
    path('Consulter/<int:sortie_id>/', views.Consulter, name='Consulter'),
    path('Modifier/<int:sortie_id>/', views.Modifier, name='Modifier'),
    path('accounts/', include('django.contrib.auth.urls'),name='login'),
    path('accounts/', include('django.contrib.auth.urls'),name='logout'),
]