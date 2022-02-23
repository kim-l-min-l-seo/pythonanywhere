from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse(
                        "<a href='https://github.com/IIBlackCode/pythonanywhere'>Github</a><br>"
                        + "<a href='http://127.0.0.1:8000/theme/index/x'>Local</a><br>"
                        + "<a href='https://www.pythonanywhere.com/'>pythonanywhere</a><br>"
                        + "<a href='https://blackcode42.pythonanywhere.com/web/theme/index/x'>배포 url</a><br>"
                        )