from django import forms
from django.forms import ModelForm, Textarea
from itineraires.models import Sortie

class SortieForm(ModelForm):
    class Meta:
        model = Sortie
        exclude = ['utilisateur','itineraire']
