from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'content': 'Furniture Store'

    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        'title': 'about',
        'content': 'About Furniture Store',
        'page_text': 'This is the about page'
    }
    return render(request, "main/about.html", context)
