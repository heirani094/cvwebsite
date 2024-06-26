from django.shortcuts import render, redirect
from website.forms import ContactForm
from django.http import HttpResponse, JsonResponse


def index_view(request):
    return render(request, 'website/index.html')


# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact')
        else:
            return redirect('/contact')
    form = ContactForm()

    return render(request, 'website/contact.html', {'form': form})


def about_view(request):
    return render(request, 'website/about.html')


def elements_view(request):
    return render(request, 'website/elements.html')


def portfolio_view(request):
    return render(request, 'website/portfolio.html')
