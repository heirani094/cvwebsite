from django.urls import path
from blog.views import *

urlpatterns = {
 #   path('test,get_image'),
    path('',blog_view),
    path('single', single_view),
}