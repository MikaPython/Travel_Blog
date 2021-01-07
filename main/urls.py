from django.contrib.sitemaps.views import index
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
]
