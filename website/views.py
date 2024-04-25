from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def home_view(request):
    return HttpResponse('<h1>This is my Home</h1>')


# Create your views here.
def contact_view(request):
    return HttpResponse('This is my Contact')


def about_view(request):
    return JsonResponse({'title': 'This is my About'})
