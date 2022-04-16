from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.Itineraire_list, name='Itineraire_list'),
    path('<int:Itineraire_id>/', views.Itineraire_DetailView, name='Itineraire_DetailView'),
    path('<int:Itineraire_id>/Editer_une_Sortie/', views.Editer_une_Sortie, name='Editer_une_Sortie'),
]