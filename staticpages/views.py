from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    return render(request, "staticpages/index.html")

# Create your views here.
