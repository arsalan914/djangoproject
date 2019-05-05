from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("hello from posts")
    context = {
        'title':'latest Posts'
    }

    return render (request, 'landing/index.html', context)
