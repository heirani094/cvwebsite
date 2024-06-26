from django.shortcuts import render, get_object_or_404
from datetime import date
from blog.models import Post
from datetime import datetime
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_view(request, cat_name=None):
    # def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1, published_date__lte=datetime.now()).order_by('-published_date')
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    # if kwargs.get('cat_name')!=None:
    # posts=posts.filter(category__name=kwargs['cat_name'])
    # if kwargs.get('author_username')!=None:
    # posts=posts.filter(author__username=kwargs['author_username'])
    posts = Paginator(posts, 3)

    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts, 'page_number': page_number}
    return render(request, 'blog/blog.html', context)


# Create your views here.
def blog_search(request):
    posts = Post.objects.filter(status=True, published_date__lte=datetime.now()).order_by('-published_date')
    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get('s'))
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def single_view(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=datetime.now())
    post.counted_view += 1
    post.save()
    previous_post = Post.objects.filter(pk__lt=post.pk, status=1, published_date__lte=timezone.now()).order_by(
        '-pk').first()
    next_post = Post.objects.filter(pk__gt=post.pk, status=1, published_date__lte=timezone.now()).order_by(
        'pk').first()
    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post
    }

    return render(request, 'blog/single.html', context)


