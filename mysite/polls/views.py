from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template import loader
from .models import Itineraire
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
    try:
        Itineraire_ = get_object_or_404(Itineraire, pk=Itineraire_id)
    except Itineraire.DoesNotExist:
        raise Http404("Itineraire does not exist")
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            Itineraire_ = Itineraire.objects.filter(title__icontains=query)
            # using HttpResponseRedirect is not appropriate here: albums must be rendered
        else:
            Itineraire_ = get_list_or_404(Itineraire)
    else:
        form = SearchForm()
    return render(request, 'polls/Itineraire_Detail.html', {'Itineraire': Itineraire_ , 'form': form})

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