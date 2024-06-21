from django.urls import path
from blog.views import *
app_name = 'blog'
urlpatterns = [
    #   path('test,get_image'),
    path('', blog_view, name='index'),
    path('<int:pid>', single_view, name='single'),
    path('category/<str:cat_name>',blog_view, name='category')
]
