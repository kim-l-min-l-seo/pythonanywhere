from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("<h1>BlackCode URL</h1>"
                        + "<a href='https://github.com/IIBlackCode/pythonanywhere'>Github</a><br>"
                        + "<a href='https://www.pythonanywhere.com/'>pythonanywhere</a><br>"
                        + "<br><br><br>"
                        + "<h1>Theme</h1>"
                        + "<a href='http://127.0.0.1:8000/theme/XXX1/0001/01'>Local Theme Admin</a><br>"
                        + "<a href='http://127.0.0.1:8000/theme/XX1X/index/x/'>Local Theme Game</a><br>"
                        + "<a href='http://127.0.0.1:8000/theme/XX11/0001/01'>Local Theme Industrious</a><br>"
                        + "<br><br><br>"
                        + "<h1>APP</h1>"
                        + "<a href='http://127.0.0.1:8000/web/index/x'>Local Theme Admin</a><br>"
                        + "<a href='http://127.0.0.1:8000/web/index/x'>Local Theme Game</a><br>"
                        + "<a href='http://127.0.0.1:8000/web/index/x'>Local Theme Industrious</a><br>"
                        + "<br><br><br>"
                        + "<h1>Server</h1>"
                        + "<a href='https://blackcode42.pythonanywhere.com/theme/index/x'>Theme URL</a><br>"
                        + "<a href='https://blackcode42.pythonanywhere.com/web/index/x'>Web URL</a><br>"
                        )