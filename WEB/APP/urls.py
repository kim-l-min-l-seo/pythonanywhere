import imp
from django.urls import path

from . import views
from .view.theme import Theme
from .view.web import Web

urlpatterns = [
    path('', views.index),
    path('theme/<menu>/<pages>/', Theme.url),
    path('web/<menu>/<pages>/', Web.url),
]
