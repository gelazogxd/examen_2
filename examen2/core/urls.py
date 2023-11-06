from django.urls import path

from core import views

from .models import *

app_name = "core"
urlpatterns = [
    ##Estadio
    path('list1/stadium/',views.List1.as_view(), name="list1"),
    path('create/Stadium/',views.CreateStadium.as_view(), name="create1"),
    path('detail/Stadium/<int:pk>/', views.DetailStadium.as_view(), name= "detailone"),
    path('update/Stadium/<int:pk>/', views.UpdateStadium.as_view(), name= "Update1"),
    path('delete/Stadium/<int:pk>/', views.DeleteStadium.as_view(), name= "delete1"),
    ##Equipo
    path('list2/team/',views.List2.as_view(), name="list2"),
    path('create2/team/',views.CreateTeam.as_view(), name="create2"),
    path('detail/team/<int:pk>/', views.DetailTeam.as_view(), name= "detailtwo"),
    path('update/team/<int:pk>/', views.UpdateTeam.as_view(), name= "Update2"),
    path('delete/team/<int:pk>/', views.DeleteTeam.as_view(), name= "delete2"),
    ##Ciudad
    path('list3/city/',views.List3.as_view(), name="list3"),
    path('create3/city/',views.CreateCity.as_view(), name="create3"),
    path('detail/city/<int:pk>/', views.DetailCity.as_view(), name= "detailthree"),
    path('update/city/<int:pk>/', views.UpdateCity.as_view(), name= "Update3"),
    path('delete/city/<int:pk>/', views.DeleteCity.as_view(), name= "delete3"),
    

    # Relacion
    path('relationships/', views.relationship_list, name='relationship_list'),

]