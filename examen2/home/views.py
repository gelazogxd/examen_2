from django.shortcuts import render
from django.views import generic

# Create your views here.

class Index(generic.View):
    template_name = "home/index.html"
    def get(self,request, *args, **kwargs):

        return render(request, self.template_name)


class Information(generic.View):
    template_name = "home/information.html"
    def get(self,request, *args, **kwargs):

        return render(request, self.template_name)

