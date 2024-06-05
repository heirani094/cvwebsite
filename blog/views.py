from django.shortcuts import render, get_object_or_404
from datetime import date
from blog.models import Post
import persian
from datetime import datetime


def convert_to_persian(text):
    text = str(text)
    text = persian.convert_ar_numbers(text)
    text = persian.convert_en_numbers(text)
    return text


def blog_view(request):
    posts = Post.objects.filter(status=1, published_date__lte=datetime.now()).order_by('-published_date')

    for post in posts:
        post.title = convert_to_persian(post.title)
        post.counted_view = convert_to_persian(post.counted_view)

    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


# Create your views here.


def single_view(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=datetime.now())
    post.counted_view += 1
    post.save()
    post.title = convert_to_persian(post.title)
    post.counted_view = convert_to_persian(post.counted_view)
    context = {'post': post}

    return render(request, 'blog/single.html', context)
