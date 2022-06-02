from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Dog, Shelter


# Create your views here.
def shelter_list(request):
    shelters = Shelter.objects.all()
    context = { 'shelters': shelters }
    return render(request, 'shelter_list.html', context)

def shelter_detail(request, pk):
    shelter = get_object_or_404(Shelter, pk=pk)
    context = {'shelter': shelter}
    return render(request, 'shelter_detail.html', context)

class DogDetailView(generic.DetailView):
    model = Dog
    template_name = 'dog_detail.html'
    context_object_name = 'dog'

from django.views import generic

from . import models


class DogCreateView(generic.CreateView):
    model = Dog
    template_name = 'dog_form.html'
    fields = ['shelter', 'name', 'description']

class DogUpdateView(generic.UpdateView):
    model = models.Dog
    template_name = 'dog_form.html'
    fields = ['shelter', 'name', 'description']