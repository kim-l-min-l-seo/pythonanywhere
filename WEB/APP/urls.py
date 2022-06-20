import imp
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .view.admin import Web as admin
from .view.game import Web as game
from .view.industrious import Web as industrious
from .view.pybo import pybo, forms
from .view.SoundExtraction import YouTube
from .view.XX11.account import Account

app_name = 'APP'

urlpatterns = [
    path('', views.index),
    
    # ============ pybo ============ #
    path('pybo/',                                   pybo.index,             name='pybo_index'),
    path('pybo/<int:question_id>/',                 pybo.detail,            name='pybo_detail'),
    path('pybo/answer/create/<int:question_id>/',   pybo.answer_create,     name='pybo_answer_create'),
    path('pybo/question/create/',                   pybo.question_create,   name='pybo_question_create'),
    
    # ============ web admin ============ #
    path('BLACKCODE/XXX1/<menu>/<pages>/'   ,admin.url),
    
    # ============ web game ============ #
    path('BLACKCODE/XX1X/<menu>/<pages>/'   ,game.url),
    path('BLACKCODE/XX1X/login/'            ,auth_views.LoginView.as_view(template_name='web/game/index.html'),  name='game_login'),
    path('BLACKCODE/XX1X/logout/'           ,auth_views.LogoutView.as_view(),                                    name='game_logout'),
    
    # ============ web industrious ============ #
    path('BLACKCODE/XX11/<menu>/<pages>/'   , industrious.url),
    path('BLACKCODE/XX11/SignUp/'           , Account.signUp, name="SignUp"),
    path('BLACKCODE/XX11/Login/'            , Account.login, name="Login"),
    
    path('down/<menu>/<url>/', YouTube.down),    
    
    
]
