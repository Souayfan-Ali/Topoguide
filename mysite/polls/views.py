from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template import loader
from .models import Itineraire,sortie
from .forms import SearchForm 
from django.http import HttpResponseRedirect

def Itineraire_list(request):
    Itineraire_list = Itineraire.objects.all()
    template = loader.get_template('polls/Itineraire_list.html')
    context = {
        'Itineraire_list': Itineraire_list,
    }
    return HttpResponse(template.render(context, request))

def Itineraire_DetailView(request, Itineraire_id):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            Date = form.cleaned_data['Date']
            Duree_reelle = form.cleaned_data['Duree_reelle']
            Nb_participants = form.cleaned_data['Nb_participants']
            Type_randonneurs = form.cleaned_data['Type_randonneurs']
            Meteo = form.cleaned_data['Meteo']
            Itineraire_ = get_object_or_404(Itineraire, pk=Itineraire_id)
            Difficulte_ressentie = form.cleaned_data['Difficulte_ressentie']
            ins = sortie(itineraire=Itineraire_,date_de_sortie=Date,duree_reelle=Duree_reelle,nombre_de_personne=Nb_participants,experience=Type_randonneurs,meteo=Meteo,difficulte=Difficulte_ressentie)
            ins.save()
        else:
            Itineraire_ = get_list_or_404(Itineraire)
    else:
        form = SearchForm()
    try:
        Itineraire_ = get_object_or_404(Itineraire, pk=Itineraire_id)
    except Itineraire.DoesNotExist:
        raise Http404("Itineraire does not exist")
    sortie_list = sortie.objects.filter(itineraire=Itineraire_)
    return render(request, 'polls/Itineraire_Detail.html', {'Itineraire': Itineraire_ , 'form': form, 'sortie_list': sortie_list})

def Editer_une_Sortie(request, Itineraire_id):
    try:
        Itineraire_ = get_object_or_404(Itineraire, pk=Itineraire_id)
    except Itineraire.DoesNotExist:
        raise Http404("Itineraire does not exist")
    template = loader.get_template('polls/Editer_une_Sortie.html')
    context = {
        'Itineraire_': Itineraire_,
    }
    return HttpResponse(template.render(context, request))