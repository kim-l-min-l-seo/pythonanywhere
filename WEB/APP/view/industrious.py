from django.http import HttpResponse
from django.shortcuts import render
from setuptools import Require

class Web :
    
    def url(request, menu, pages):
        url = 'BLACKCODE'
        web = 'XX11'
        ver = 'VER 1.0.0'
        print("menu : ", menu)
        print("page : ",pages)
        
        if (menu == "index" or menu == "0000") and pages == "XX":
            context = {
                'url'   : url, 
                'menu'  : menu,
                'title' : '',
                'ver'   : ver
            }
            return render(request, './'+url+'/'+web+'/0000_index.html', context)
        
        elif menu == "0001" :
            if pages == "XX" :
                context = {
                    'url' : url,
                    'menu': menu,
                    'title':'회원가입',
                    'ver'   : ver
                }
                # return render(request, './'+url+'/'+web+'/generic.html', context)
                return render(request, './'+url+'/'+web+'/0001/popupJoin.html', context)  
            elif pages == "Join" :
                context = {
                    'url' : url,
                    'menu': menu,
                    'title':'회원가입',
                    'ver'   : ver
                }
                return render(request, './'+url+'/'+web+'/0001/popupJoin.html', context)
            elif pages == "Login" :
                context = {
                    'url' : url,
                    'menu': menu,
                    'title':'로그인',
                    'ver'   : ver
                }
                return render(request, './'+url+'/'+web+'/0001/popupLogin.html', context) 
            
        elif menu == "0010" :
            if pages == "XX":
                context = {
                    'url' : url,
                    'menu': menu,
                    'title':'Generic Page',
                    'ver'   : ver
                }
                return render(request, './'+url+'/'+web+'/generic.html', context)
            elif pages == "00" :
                context = {
                    'url' : url,
                    'menu': menu,
                    'title':'회원관리[관리자전용]',
                    'ver'   : ver
                }
                return render(request, './'+url+'/'+web+'/0010/00.html', context)
            elif pages == "01" :
                context = {
                    'url' : url,
                    'menu': menu,
                    'title':'Profile',
                    'ver'   : ver
                }
                return render(request, './'+url+'/'+web+'/0010/01.html', context)
        
        
        elif (menu == "ReleaseNote" or menu == "1111") and pages == "XX":
            context = {
                'url' : url,
                'menu': menu,
                'title':'Release Note',
                'ver'   : ver
            }
            return render(request, './'+url+'/'+web+'/1111_Release Note.html', context)
        elif menu == "9999" and pages == "XX":
            context = {
                'url' : url,
                'menu': menu,
                'title':'Elements',
                'ver'   : ver
            }
            return render(request, './'+url+'/'+web+'/9999_elements.html', context)
        
        else : 
            # return HttpResponse("개발 진행중 2022.02.22 "+menu)
            return render(request, './'+url+'/404.html')
        