from django.http import HttpResponse
from django.shortcuts import render
from setuptools import Require

class Theme :
    
    def url(request, menu, pages):
        print("title : ",menu)
        print("page : ",pages)
        
        context = {
            'url' : "theme",
            'menu': menu,
            'pages': pages,
        }
        
        if (menu == "index" or menu == "0001") and pages == "01":
            context = {'menu': menu,'title':'Industrious by TEMPLATED'}   
            return render(request, './theme/industrious/index.html', context)
        elif menu == "0010" and pages == "01":
            context = {'menu': menu,'title':'Generic Page - Industrious by TEMPLATED'}
            return render(request, './theme/industrious/generic.html', context)
        elif menu == "0011" and pages == "01":
            context = {'menu': menu,'title':'Elements - Industrious by TEMPLATED'}
            return render(request, './theme/industrious/elements.html', context)
        
        else : 
            # return HttpResponse("개발 진행중 2022.02.22 "+menu)
            return render(request, './theme/404.html', context)
        