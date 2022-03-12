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
            context = {'menu': menu,'title':'Alerts'}   
            return render(request, './theme/admin/01/01.html', context)
        elif menu == "0010" and pages == "01":
            context = {'menu': menu,'title':'Profile'}
            return render(request, './theme/admin/02/01.html', context)
        elif menu == "0011" and pages == "01":
            context = {'menu': menu,'title':'Settings'}
            return render(request, './theme/admin/03/01.html', context)
        elif menu == "0100" and pages == "01":
            context = {'menu': menu,'title':'Invoice'}
            return render(request, './theme/admin/04/01.html', context)
        elif menu == "0101" and pages == "01":
            context = {'menu': menu,'title':'Blank'}
            return render(request, './theme/admin/05/01.html', context)
        elif menu == "0110":
            if pages == "01":
                context = {'menu': menu,'title':'Alerts'}
                return render(request, './theme/admin/06/01.html', context)
            elif pages == "02":
                context = {'menu': menu,'title':'Buttons'}
                return render(request, './theme/admin/06/02.html', context)
            elif pages == "03":
                context = {'menu': menu,'title':'Cards'}
                return render(request, './theme/admin/06/03.html', context)
            elif pages == "04":
                context = {'menu': menu,'title':'General'}
                return render(request, './theme/admin/06/04.html', context)
            elif pages == "05":
                context = {'menu': menu,'title':'Grid'}
                return render(request, './theme/admin/06/05.html', context)
            elif pages == "06":                
                context = {'menu': menu,'title':'Modals'}
                return render(request, './theme/admin/06/06.html', context)
            elif pages == "07":
                context = {'menu': menu,'title':'Typography'}
                return render(request, './theme/admin/06/07.html', context)
        elif menu == "0111" and pages == "01":
            context = {'menu': menu,'title':'Feather'}
            return render(request, './theme/admin/07/01.html', context)
        elif menu == "1000": 
            if pages == "01":
                context = {'menu': menu,'title':'Form Layouts'}
                return render(request, './theme/admin/08/01.html', context)
            if pages == "02":
                context = {'menu': menu,'title':'Basic Inputs'}
                return render(request, './theme/admin/08/02.html', context)
        elif menu == "1001" and pages == "01":
            context = {'menu': menu,'title':'Basic Tables'}
            return render(request, './theme/admin/09/01.html', context)
        elif menu == "1010" and pages == "01":
            context = {'menu': menu,'title':'Chart.js'}
            return render(request, './theme/admin/10/01.html', context)
        elif menu == "1011" and pages == "01":
            context = {'menu': menu,'title':'Google Maps'}
            return render(request, './theme/admin/11/01.html', context)
        else : 
            # return HttpResponse("개발 진행중 2022.02.22 "+menu)
            return render(request, './theme/404.html', context)
        