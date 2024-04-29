from django.shortcuts import render



def blog_view(request):
    return render(request, 'blog/blog.html')


# Create your views here.
def single_view(request):
    return render(request, 'blog/single.html')
