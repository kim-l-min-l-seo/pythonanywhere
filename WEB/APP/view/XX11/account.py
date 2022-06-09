from tkinter import E
from tkinter.messagebox import NO
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse ,JsonResponse
from datetime import timedelta, date, time, datetime
import sqlite3


currentTime = datetime.now().strftime('%Y-%m-%d')
class Account:
    
    def signUp(request):
        conn = sqlite3.connect("db.sqlite3",check_same_thread=False)
        cur = conn.cursor()

        if request.method == 'POST':
            
            test = request.POST.get("test");
            print(">>> ",test)
            print("currentTime",currentTime)
            
            email       = request.POST.get("email");
            birth       = request.POST.get("birth");
            name        = request.POST.get("name");
            nickName    = request.POST.get("nickName");
            profile     = request.POST.get("profile");
            phoneNumber = request.POST.get("phoneNumber");
            password    = request.POST.get("password");
            password2   = request.POST.get("password2");
            
            print("email        >>> ",email)
            print("birth        >>> ",birth)
            print("name         >>> ",name)
            print("nickName     >>> ",nickName)
            print("profile      >>> ",profile)
            print("phoneNumber  >>> ",phoneNumber)
            print("password     >>> ",password)
            print("password2    >>> ",password2)

            with conn:
                cur.execute("select count(*) from auth_user ")
                total = cur.fetchone()
                print('총 수강생 수 : ',total[0])
            try :
                with conn:
                    cur.execute("insert into auth_user (email, password, username, first_name, last_name, is_superuser, is_staff, is_active, date_joined) values ('"+email+"','"+password+"','"+name+"', '"+name+"', '"+name+"', '3', '3', '3', '"+currentTime+"') ")
                    curfet = cur.fetchone()
                    print("curfet :",curfet)
            except Exception as e:
                print('Exception : ',e)
                context = {"result" : False}
            return JsonResponse(context,status = 400)
                
        return JsonResponse(context,status=200)