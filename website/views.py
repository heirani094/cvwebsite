from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index_view(request):
    return render(request, 'website/index.html')


# Create your views here.
def contact_view(request):
    return render(request, 'website/contact.html')


def about_view(request):
    return render(request, 'website/about.html')


def get_image(request):
    with open('path/to/image.jpg', 'rb') as f:
        image_data = f.read()
    return HttpResponse(image_data, content_type="image/jpeg")
