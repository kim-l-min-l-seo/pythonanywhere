import imp
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

from .view.admin    import Theme as AdminTheme
from .view.game     import Theme as GameTheme

app_name = 'THEME'

urlpatterns = [
    # path('', views.index),
    
    path('admin/<menu>/<pages>/',   AdminTheme.url),
    path('game/<menu>/<pages>/',    GameTheme.url),
    
    path('web/login/', auth_views.LoginView.as_view(template_name='web/index.html'), name='login'),
    path('web/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
