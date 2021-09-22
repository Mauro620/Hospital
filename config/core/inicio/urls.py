from django.urls import path

from core.inicio.views import *
urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),

]
