from django import forms

from .models import *


class StadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields = "__all__"
        exclude = ["num"]
        widgets = {
            "estadio": forms.TextInput(attrs={"type": "text", "class": "form-control", "placeholder": "Ingrese el número del estadio"}),
            "nombre": forms.TextInput(attrs={"type": "text", "class": "form-control", "placeholder": "Ingrese el nombre del estadio"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Ingrese la descripción del estadio"}),
        }

class UpdateStadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields = "__all__"
        exclude = ["num"]
        widgets = {
            "estadio": forms.TextInput(attrs={"type": "text", "class": "form-control", "placeholder": "Ingrese el número del estadio"}),
            "nombre": forms.TextInput(attrs={"type": "text", "class": "form-control", "placeholder": "Ingrese el nombre del estadio"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Ingrese la descripción del estadio"}),
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"
        exclude = ["codigo"]
        widgets = {
            "equipo": forms.TextInput(attrs={"type": "text", "class": "form-control", "placeholder": "Ingrese el nombre del equipo"}),
            "liga": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Ingrese la descripción de la liga"}),
        }

class UpdateTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"
        exclude = ["codigo"]
        widgets = {
            "equipo": forms.TextInput(attrs={"type": "text", "class": "form-control", "placeholder": "Ingrese el nombre del equipo"}),
            "liga": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Ingrese la descripción de la liga"}),
        }

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = "__all__"
        exclude = ["id"]
        widgets = {
            "ciudad": forms.TextInput(attrs={"type": "text", "class": "form-control", "placeholder": "Ingrese el nombre de la ciudad"}),
        }


class UpdateCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = "__all__"
        exclude = ["id"]
        widgets = {
            "ciudad": forms.TextInput(attrs={"type": "text", "class": "form-control", "placeholder": "Ingrese el nombre de la ciudad"}),
        }

class RelationshipForm(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
