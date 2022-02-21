import imp
from django.urls import path

from . import views
from .view.theme import Theme

urlpatterns = [
    path('', views.index),
    path('theme/<page>/', Theme.theme),
]
