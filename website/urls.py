from django.urls import path
from website.views import *

urlpatterns = {
 #   path('test,get_image'),
    path('',index_view),
    path('contact', contact_view),
    path('about', about_view)
}
