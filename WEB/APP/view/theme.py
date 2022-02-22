from django.http import HttpResponse
from django.shortcuts import render
from setuptools import Require

class Theme :
    
    def theme(request, html):
        print("html : ",html)
        
        context = {
            'html' : html
        }
        
        if html == "index":   
            return render(request, './theme/index.html', context)
        elif html == "main":
            return render(request, './theme/main.html', context)
        elif html == "pages":
            return render(request, './theme/main.html', context)
        elif html == "main":
            return render(request, './theme/main.html', context)
        elif html == "main":
            return render(request, './theme/main.html', context)
        elif html == "main":
            return render(request, './theme/main.html', context)
        elif html == "main":
            return render(request, './theme/main.html', context)
        elif html == "main":
            return render(request, './theme/main.html', context)
        else : 
            return HttpResponse("개발 진행중 2022.02.22 "+page)
        