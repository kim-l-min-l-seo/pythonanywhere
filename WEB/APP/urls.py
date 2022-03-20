import imp
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .view.web import Web

app_name = 'APP'

urlpatterns = [
    path('', views.index),
    path('web/<menu>/<pages>/', Web.url),
    path('web/login/',  auth_views.LoginView.as_view(template_name='web/game/index.html'),  name='game_login'),
    path('web/logout/', auth_views.LogoutView.as_view(),                                    name='game_logout'),
]
