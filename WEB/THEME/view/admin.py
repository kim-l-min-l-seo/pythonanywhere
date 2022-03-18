from django.http import HttpResponse
from django.shortcuts import render
from setuptools import Require

class Theme :
    
    def url(request, menu, pages):
        print("menu : ", menu)
        print("page : ",pages)
        
        url = 'theme';
        html = 'XXX1'
        
        context = {
            'url': url,
            'html' : html,
            'menu': menu,
            'pages': pages,
        }
        
        if html == 'XXX1':
            fileName = 'admin'
        elif html == 'XX1X':
            fileName = 'game'
        elif html == 'XX11':
            fileName = 'industrious'
        
        # HTML path = url/filename(html)/menu/pages
        print("URL : ", './'+url+'/'+fileName+'/'+menu+'(2)/'+pages+'.html')
        
        if (menu == "index" or menu == "0001") and pages == "01":
            context['title'] = 'Alerts'
            return render(request, './'+url+'/'+fileName+'/01/01.html', context)
        elif menu == "0010" and pages == "01":
            context['title'] = 'Profile'
            return render(request, './'+url+'/'+fileName+'/02/01.html', context)
        elif menu == "0011" and pages == "01":
            context['title'] = 'Settings'
            return render(request, './'+url+'/'+fileName+'/03/01.html', context)
        elif menu == "0100" and pages == "01":
            context['title'] = 'Invoice'
            return render(request, './'+url+'/'+fileName+'/04/01.html', context)
        elif menu == "0101" and pages == "01":
            context['title'] = 'Blank'
            return render(request, './'+url+'/'+fileName+'/05/01.html', context)
        elif menu == "0110":
            if pages == "01":
                context['title'] = 'Alerts'
                return render(request, './'+url+'/'+fileName+'/06/01.html', context)
            elif pages == "02":
                context['title'] = 'Buttons'
                return render(request, './'+url+'/'+fileName+'/06/02.html', context)
            elif pages == "03":
                context['title'] = 'Cards'
                return render(request, './'+url+'/'+fileName+'/06/03.html', context)
            elif pages == "04":
                context['title'] = 'General'
                return render(request, './'+url+'/'+fileName+'/06/04.html', context)
            elif pages == "05":
                context['title'] = 'Grid'
                return render(request, './'+url+'/'+fileName+'/06/05.html', context)
            elif pages == "06":
                context['title'] = 'Modals'
                return render(request, './'+url+'/'+fileName+'/06/06.html', context)
            elif pages == "07":
                context['title'] = 'Typography'
                return render(request, './'+url+'/'+fileName+'/06/07.html', context)
        elif menu == "0111" and pages == "01":
            context['title'] = 'Feather'
            return render(request, './'+url+'/'+fileName+'/07/01.html', context)
        elif menu == "1000": 
            if pages == "01":
                context['title'] = 'Form Layouts'
                return render(request, './'+url+'/'+fileName+'/08/01.html', context)
            if pages == "02":
                context['title'] = 'Basic Inputs'
                return render(request, './'+url+'/'+fileName+'/08/02.html', context)
        elif menu == "1001" and pages == "01":
            context['title'] = 'Basic Tables'
            return render(request, './'+url+'/'+fileName+'/09/01.html', context)
        elif menu == "1010" and pages == "01":
            context['title'] = 'Chart.js'
            return render(request, './'+url+'/'+fileName+'/10/01.html', context)
        elif menu == "1011" and pages == "01":
            context['title'] = 'Google Maps'
            return render(request, './'+url+'/'+fileName+'/11/01.html', context)
        else : 
            # return HttpResponse("개발 진행중 2022.02.22 "+menu)
            context['title'] = 'Feather'
            return render(request, './'+url+'/'+fileName+'/404.html', context)
        