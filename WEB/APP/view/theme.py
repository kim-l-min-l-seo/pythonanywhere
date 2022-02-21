from django.http import HttpResponse
from django.shortcuts import render
from setuptools import Require

class Theme :
    
    def theme(request, page):
        print("PAGE : ",page)
        page ='Home'
        context = {
            'page' : page
        }
        
        if page == "index":   
            return render(request, './theme/index.html', context)
        else : 
            return HttpResponse("개발 진행중 2022.02.22")
        