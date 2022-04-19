from django import forms

class SortieForm(forms.Form):
    Date = forms.DateTimeField()
    Duree_reelle = forms.CharField(label='Duree reelle', max_length=100, required=False)
    Nb_participants = forms.IntegerField(label='Nb participants',required=False)
    Type_randonneurs = forms.CharField(max_length=100, required=False)
    Meteo = forms.CharField(max_length=100, required=False)
    Difficulte_ressentie = forms.IntegerField(required=False)
    commentaire =forms.CharField(required=False)