
from django.urls import path
from website.views import *

urlpatterns = {

    path('test', test_http)
}