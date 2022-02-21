from django.http import HttpResponse
from django.shortcuts import render

class Theme :
    def theme(request, page):
        print("PAGE : ",page)
        page ='Home'
        context = {
            'page' : page
        }
        
        if page == "index":   
            return render(request, './theme/index.html', context)