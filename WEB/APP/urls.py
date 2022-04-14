import imp
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .view.web import Web
from .view.pybo import pybo, forms
from .view.SoundExtraction import YouTube

app_name = 'APP'

urlpatterns = [
    path('', views.index),
    
    # ============ pybo ============ #
    path('pybo/',                                   pybo.index,             name='pybo_index'),
    path('pybo/<int:question_id>/',                 pybo.detail,            name='pybo_detail'),
    path('pybo/answer/create/<int:question_id>/',   pybo.answer_create,     name='pybo_answer_create'),
    path('pybo/question/create/',                   pybo.question_create,   name='pybo_question_create'),
    
    # ============ web  ============ #
    path('web/<menu>/<pages>/', Web.url),
    path('web/login/',  auth_views.LoginView.as_view(template_name='web/game/index.html'),  name='game_login'),
    path('web/logout/', auth_views.LogoutView.as_view(),                                    name='game_logout'),
    
    # ============ web  ============ #
    path('down/<menu>/<url>/', YouTube.down),    
]
