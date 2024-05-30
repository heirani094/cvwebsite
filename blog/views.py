from django.shortcuts import render,get_object_or_404

from blog.models import Post


def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


# Create your views here.
def single_view(request):
    return render(request, 'blog/single.html')

def single_view(request,pid):
    post =get_object_or_404(Post,pk=pid ,status=1)
    context = {'post':post}
    return render(request, 'blog/single.html', context)