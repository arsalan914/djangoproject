from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from .models import Project, Picture
# Create your views here.


# def index(request):
#     return HttpResponse("sk project index")

class IndexView(generic.ListView):
    template_name = 'sk/index.html'
    context_object_name = 'all_projects'

    def get_queryset(self):
        return Project.objects.all()


class DetailsView(generic.DetailView):
    model = Project
    template_name = 'sk/details.html'
