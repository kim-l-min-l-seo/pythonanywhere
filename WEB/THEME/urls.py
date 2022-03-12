import imp
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

from .view.game import Theme

app_name = 'THEME'

urlpatterns = [
    # path('', views.index),
    
    path('admin/<menu>/<pages>/', Theme.url),
    path('game/<menu>/<pages>/', Theme.url),
    
    path('web/login/', auth_views.LoginView.as_view(template_name='web/index.html'), name='login'),
    path('web/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
