from django.urls import path
from core.base.views import *

urlpatterns = [
    path('', inicio, name='base'),
]