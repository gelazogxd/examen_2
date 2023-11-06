from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import *
from .models import *

# Create your views here.

##Estadio

class List1(generic.View):
    template_name = "core/list1.html"
    context = {}

    def get(self, request, *args, **kwargs):
        queryset = Stadium.objects.all()
        self.context = {
            "stadiums": queryset  
        }
        return render(request, self.template_name, self.context)



class DetailStadium(generic.DetailView):
    template_name = "core/detail1.html"
    model = Stadium


class CreateStadium(generic.CreateView):
    template_name = "core/create1.html"
    model = Stadium
    form_class = StadiumForm
    success_url = reverse_lazy("core:list1")


class UpdateStadium(generic.UpdateView):
    template_name = "core/Update1.html"
    model = Stadium
    form_class = UpdateStadiumForm
    success_url = reverse_lazy("core:list1")

class DeleteStadium(generic.DeleteView):
    template_name = "core/delete1.html"
    model = Stadium
    success_url = reverse_lazy("core:list1")


##Equipos

class List2(generic.View):
    template_name = "core/list2.html"
    context = {}

    def get(self, request, *args, **kwargs):
        queryset = Team.objects.all()
        self.context = {
            "Team": queryset
        }
        return render(request, self.template_name,self.context)
    
class CreateTeam(generic.CreateView):
    template_name = "core/create_team.html"
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("core:list_teams")

    def form_valid(self, form):
        # Aquí puedes realizar operaciones adicionales si es necesario
        return super().form_valid(form)




class DetailTeam(generic.DetailView):
    template_name = "core/detail2.html"
    model = Team

class UpdateTeam(generic.UpdateView):
    template_name = "core/Update2.html"
    model = Team
    form_class = UpdateTeamForm
    success_url = reverse_lazy("core:list2")

class DeleteTeam(generic.DeleteView):
    template_name = "core/delete2.html"
    model = Team
    success_url = reverse_lazy("core:list2")

##Ciudades

class List3(generic.View):
    template_name = "core/list3.html"
    context = {}

    def get(self, request, *args, **kwargs):
        queryset = City.objects.all()
        self.context = {
            "City": queryset
        }
        return render(request, self.template_name,self.context)

class CreateCity(generic.CreateView):
    template_name = "core/create3.html"
    model = City
    form_class = CityForm
    success_url = reverse_lazy("core:list3")

class DetailCity(generic.DetailView):
    template_name = "core/detail3.html"
    model = City

class UpdateCity(generic.UpdateView):
    template_name = "core/Update3.html"
    model = City
    form_class = UpdateCityForm
    success_url = reverse_lazy("core:list3")

class DeleteCity(generic.DeleteView):
    template_name = "core/delete3.html"
    model = City
    success_url = reverse_lazy("core:list3")
    
    

def relationship_list(request):
    relationships = Relationship.objects.all()
    print(relationships)  # Imprime las relaciones en la consola del servidor
    return render(request, 'core/relationship_list.html', {'relationships': relationships})