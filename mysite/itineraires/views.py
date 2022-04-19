from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template import loader
from .models import Itineraire,sortie
from .forms import SortieForm 
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def Itineraire_list(request):
    Itineraire_list = Itineraire.objects.all()
    template = loader.get_template('itineraires/Itineraire_list.html')
    context = {
        'Itineraire_list': Itineraire_list,
    }
    return HttpResponse(template.render(context, request))

def Itineraire_DetailView(request, Itineraire_id):
    if request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid():
            utilisateur=request.user.username
            Date = form.cleaned_data['Date']
            Duree_reelle = form.cleaned_data['Duree_reelle']
            Nb_participants = form.cleaned_data['Nb_participants']
            Type_randonneurs = form.cleaned_data['Type_randonneurs']
            Meteo = form.cleaned_data['Meteo']
            Itineraire_ = get_object_or_404(Itineraire, pk=Itineraire_id)
            Difficulte_ressentie = form.cleaned_data['Difficulte_ressentie']
            commentaire = form.cleaned_data['commentaire']
            ins = sortie(utilisateur=utilisateur,itineraire=Itineraire_,date_de_sortie=Date,duree_reelle=Duree_reelle,nombre_de_personne=Nb_participants,experience=Type_randonneurs,meteo=Meteo,difficulte=Difficulte_ressentie,commentaire=commentaire)
            ins.save()
        else:
            Itineraire_ = get_list_or_404(Itineraire)
    else:
        form = SortieForm()
    try:
        Itineraire_ = get_object_or_404(Itineraire, pk=Itineraire_id)
    except Itineraire.DoesNotExist:
        raise Http404("Itineraire does not exist")
    sortie_list = sortie.objects.filter(itineraire=Itineraire_)
    return render(request, 'itineraires/Itineraire_Detail.html', {'Itineraire': Itineraire_ , 'form': form, 'sortie_list': sortie_list})

def Ajouter_une_Sortie(request, Itineraire_id):
    try:
        Itineraire_ = get_object_or_404(Itineraire, pk=Itineraire_id)
    except Itineraire_.DoesNotExist:
        raise Http404("Itineraire does not exist")
    template = loader.get_template('itineraires/Ajouter_une_Sortie.html')
    context = {
        'Itineraire_': Itineraire_,
    }
    return HttpResponse(template.render(context, request))

def Consulter(request, sortie_id):
    try:
        sortie_ = get_object_or_404(sortie, pk=sortie_id)
    except sortie_.DoesNotExist:
        raise Http404("sortie does not exist")
    template = loader.get_template('itineraires/Consulter.html')
    context = {
        'sortie_': sortie_
    }
    return HttpResponse(template.render(context, request))

def Modifier(request, sortie_id):
    try:
        sortie1 = get_object_or_404(sortie, pk=sortie_id)
    except sortie1.DoesNotExist:
        raise Http404("sortie does not exist")
    if request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid():
            sortie1.date_de_sortie = form.cleaned_data['Date']
            sortie1.Duree_reelle = form.cleaned_data['Duree_reelle']
            sortie1.nombre_de_personne = form.cleaned_data['Nb_participants']
            sortie1.experience = form.cleaned_data['Type_randonneurs']
            sortie1.meteo = form.cleaned_data['Meteo']
            sortie1.difficulte = form.cleaned_data['Difficulte_ressentie']
            sortie1.commentaire = form.cleaned_data['commentaire']
            sortie1.save()
        else:
            sortie1 = get_list_or_404(sortie)
    else:
        form = SortieForm()
    sortie1 = get_object_or_404(sortie, pk=sortie_id)
    Itineraire1= get_object_or_404(Itineraire, pk=sortie1.itineraire.id)
    sortie_list = sortie.objects.filter(itineraire=Itineraire1.id)
    return render(request, 'itineraires/Itineraire_Detail.html', {'Itineraire': Itineraire1 , 'form': form, 'sortie_list': sortie_list})