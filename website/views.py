from django.shortcuts import render
from django.http import HttpResponse


def test_http(request):
    return HttpResponse("dali")

# Create your views here.
