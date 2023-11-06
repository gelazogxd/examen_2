from django.urls import path
from home import views

app_name = "home"
urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('information/', views.Information.as_view(), name="information")
]