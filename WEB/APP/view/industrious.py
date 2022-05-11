from django.http import HttpResponse
from django.shortcuts import render
from setuptools import Require

class Web :
    
    def url(request, menu, pages):
        url = 'BLACKCODE'
        web = 'XX11'
        print("menu : ", menu)
        print("page : ",pages)
        
        if (menu == "index" or menu == "0000") and pages == "XX":
            context = {
                'url': url, 
                'menu': menu,
                'title': ''
            }
            return render(request, './'+url+'/'+web+'/0000_index.html', context)
        elif menu == "0010" and pages == "XX":
            context = {
                'url' : url,
                'menu': menu,
                'title':'Generic Page'
            }
            return render(request, './'+url+'/'+web+'/generic.html', context)
        
        
        
        elif (menu == "ReleaseNote" or menu == "1111") and pages == "XX":
            context = {
                'url' : url,
                'menu': menu,
                'title':'Release Note'
            }
            return render(request, './'+url+'/'+web+'/1111_Release Note.html', context)
        elif menu == "9999" and pages == "XX":
            context = {
                'url' : url,
                'menu': menu,
                'title':'Elements'
            }
            return render(request, './'+url+'/'+web+'/elements.html', context)
        
        else : 
            # return HttpResponse("개발 진행중 2022.02.22 "+menu)
            return render(request, './'+url+'/404.html')
        