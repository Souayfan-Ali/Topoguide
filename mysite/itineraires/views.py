from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template import loader
from .models import Itineraire,Sortie
from .forms import SortieForm 
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def Itineraire_list(request):
    itineraire_list = Itineraire.objects.all()
    template = loader.get_template('itineraires/Itineraire_list.html')
    context = {
        'itineraire_list': itineraire_list,
    }
    return HttpResponse(template.render(context, request))

def Itineraire_DetailView(request, itineraire_id):
    try:
        itineraire_ = get_object_or_404(Itineraire, pk=itineraire_id)
    except itineraire_.DoesNotExist:
        raise Http404("Itineraire does not exist")
    sortie_list = Sortie.objects.filter(itineraire=itineraire_)
    return render(request, 'itineraires/Itineraire_Detail.html',
     {'itineraire': itineraire_ ,
     'sortie_list': sortie_list,
    'img_url':"itineraires/images/"+str(itineraire_.id)+".jpg"})

def Ajouter_une_Sortie(request, itineraire_id):
    try:
        itineraire_ = get_object_or_404(Itineraire, pk=itineraire_id)
    except itineraire_.DoesNotExist:
        raise Http404("Itineraire does not exist")
    if request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid():
            sortie_new = form.save(commit=False)
            sortie_new.itineraire=itineraire_
            sortie_new.utilisateur=request.user
            sortie_new.save()
            sortie_list = Sortie.objects.filter(itineraire=itineraire_)
            return render(request, 'itineraires/Itineraire_Detail.html', 
            {'itineraire': itineraire_,
            'form': form, 
            'sortie_list': sortie_list,
            'img_url':"itineraires/images/"+str(itineraire_.id)+".jpg"})
    else:
        form = SortieForm()
    template = loader.get_template('itineraires/Ajouter_une_Sortie.html')
    context = {
        'itineraire_': itineraire_,
    }
    return HttpResponse(template.render(context, request))

def Consulter(request, sortie_id):
    try:
        sortie_ = get_object_or_404(Sortie, pk=sortie_id)
    except sortie_.DoesNotExist:
        raise Http404("sortie does not exist")
    template = loader.get_template('itineraires/Consulter.html')
    Itineraire_= get_object_or_404(Itineraire, pk=sortie_.itineraire.id)
    context = {
        'sortie_': sortie_,
        'img_url':"itineraires/images/"+str(Itineraire_.id)+".jpg"
    }
    return HttpResponse(template.render(context, request))

def Modifier(request, sortie_id):
    try:
        sortie1 = get_object_or_404(Sortie, pk=sortie_id)
    except sortie1.DoesNotExist:
        raise Http404("sortie does not exist")
    if request.method == 'POST':
        form = SortieForm(request.POST,instance=sortie1)
        if form.is_valid():
            sortie_updated = form.save(commit=False)
            sortie_updated.save()
            print("adkfjdlksjalfs")
        else:
            sortie1 = get_object_or_404(Sortie, pk=sortie_id)
    else:
        form = SortieForm()
    itineraire1= get_object_or_404(Itineraire, pk=sortie1.itineraire.id)
    sortie_list = Sortie.objects.filter(itineraire=itineraire1.id)
    return render(request, 'itineraires/Itineraire_Detail.html', 
    {'itineraire': itineraire1 ,
    'form': form, 
    'sortie_list': sortie_list,
    'img_url':"itineraires/images/"+str(itineraire1.id)+".jpg"})