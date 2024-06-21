from django import template
from blog.models import Post, Category, Advertisement
from datetime import datetime
import jdatetime

register = template.Library()


@register.filter
def to_jalali(date):
    if not date:
        return ''
    jalali_date = jdatetime.datetime.fromgregorian(datetime=date)
    return jalali_date.strftime('%Y/%m/%d')


@register.filter
def to_persian_numerals(value):
    persian_numbers = {
        '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
        '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'
    }
    return ''.join(persian_numbers[digit] if digit in persian_numbers else digit for digit in str(value))


# {{% totalposts %}}
# @register.simple_tag(name='totalposts')
# def function():
#   return Post.objects.filter(status=1).count()


# {{post.content|snippet:50}}
@register.filter
def snippet(value, arg=20):
    return value[:arg] + "..."


# {% popularposts %}
@register.inclusion_tag('blog/popular-posts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1, published_date__lte=datetime.now()).order_by('published_date')[:arg]
    return {'posts': posts}


#
@register.inclusion_tag('blog/categories-posts.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}


@register.simple_tag
def get_ads():
    return Advertisement.objects.all()
