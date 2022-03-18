from django.http import HttpResponse
from django.shortcuts import render
from setuptools import Require

class Theme :
    
    def url(request, menu, pages):
        url = 'theme'
        print("menu : ", menu)
        print("page : ",pages)
        
        if (menu == "index" or menu == "0001") and pages == "01":
            context = {
                'url': url, 
                'menu': menu,
                'title': ''
            }
            return render(request, './'+url+'/industrious/index.html', context)
        elif menu == "0010" and pages == "01":
            context = {
                'url' : url,
                'menu': menu,
                'title':'Generic Page'
            }
            return render(request, './'+url+'/industrious/generic.html', context)
        elif menu == "0011" and pages == "01":
            context = {
                'url' : url,
                'menu': menu,
                'title':'Elements'
            }
            return render(request, './'+url+'/industrious/elements.html', context)
        
        else : 
            # return HttpResponse("개발 진행중 2022.02.22 "+menu)
            return render(request, './'+url+'/404.html', context)
        