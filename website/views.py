from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index_view(request):
    return render(request, 'website/index.html')


# Create your views here.
def contact_view(request):
    return render(request, 'website/contact.html')


def about_view(request):
    return render(request, 'website/about.html')

def elements_view(request):
    return render(request, 'website/elements.html')

def portfolio_view(request):
    return render(request, 'website/portfolio.html')


