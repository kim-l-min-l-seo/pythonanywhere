from django.http import HttpResponse
from django.shortcuts import render
from setuptools import Require

class Theme :
    
    def url(request, menu, pages):
        print("menu : ",menu)
        print("page : ",pages)
        
        context = {
            'url' : "theme",
            'menu': menu,
            'pages': pages,
        }
        
        if (menu == "index" or menu == "home") and pages == "x":   
            return render(request, './theme/index.html', context)
       
        else : 
            # return HttpResponse("개발 진행중 2022.02.22 "+menu)
            return render(request, './theme/404.html', context)
        