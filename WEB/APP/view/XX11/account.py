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

            context = {"test" : True}
            if email == None:
                context = {"result" : False}
                return JsonResponse(context,status=400)
            with conn:
                cur.execute("select count(*) from auth_user ")
                total = cur.fetchone()
                print('총 수강생 수 : ',total[0])
            return JsonResponse(context,status=200)
        return JsonResponse(context,status=200)