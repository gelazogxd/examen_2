from django.contrib import admin

from .models import City, Stadium, Team


@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = [
        "num",
        "estadio",
        "nombre",
        "description",
    ]

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = [
        "codigo",
        "equipo",
        "liga",
    ]

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "ciudad",
    ]
