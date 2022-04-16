from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Itineraire


def Itineraire_list(request):
    Itineraire_list = Itineraire.objects.all()
    template = loader.get_template('polls/itineraire_list.html')
    context = {
        'Itineraire_list': Itineraire_list,
    }
    return HttpResponse(template.render(context, request))

def Itineraire_DetailView(request, Itineraire_id):
    try:
        Itineraire_ = get_object_or_404(Itineraire, pk=Itineraire_id)
    except Itineraire.DoesNotExist:
        raise Http404("Itineraire does not exist")
    return render(request, 'polls/Itineraire_Detail.html', {'Itineraire': Itineraire_})