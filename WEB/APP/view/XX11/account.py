from asyncio.windows_events import NULL
from tkinter import E
from tkinter.messagebox import NO
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse ,JsonResponse
from datetime import timedelta, date, time, datetime
import sqlite3

Querry = ""

currentTime = datetime.now().strftime('%Y-%m-%d')
class Account:
    
    def signUp(request):
        conn = sqlite3.connect("db.sqlite3",check_same_thread=False)
        cur = conn.cursor()

        if request.method == 'POST':
            
            test = request.POST.get("test");
            print(">>> ",test)
            print("currentTime",currentTime)
            
            # 1. Data POST방식 수신
            email       = request.POST.get("email");
            birth       = request.POST.get("birth");
            username    = request.POST.get("name");
            nickName    = request.POST.get("nickName");
            profile     = request.POST.get("profile");
            phoneNumber = request.POST.get("phoneNumber");
            password    = request.POST.get("password");
            password2   = request.POST.get("password2");
            
            print("email        >>> ",email)
            print("birth        >>> ",birth)
            print("username     >>> ",username)
            print("nickName     >>> ",nickName)
            print("profile      >>> ",profile)
            print("phoneNumber  >>> ",phoneNumber)
            print("password     >>> ",password)
            print("password2    >>> ",password2)

            # 2. Data Check
            if email == None or email == "":
                msg = "Please enter your email address"
                print(msg)
                context = {
                        "result"    : False,
                        "msg"       : msg
                        }
                return JsonResponse(context)
            if username == None or username == "":
                msg = "Please enter your Name"
                print(msg)
                context = {
                        "result"    : False,
                        "msg"       : msg
                        }
                return JsonResponse(context)
            if phoneNumber == None or phoneNumber == "":
                msg = "Please enter your phoneNumber"
                print(msg)
                context = {
                        "result"    : False,
                        "msg"       : msg
                        }
                return JsonResponse(context)
            if (password != password2) or password == None or password == "" or password2 == None or password2 == "":
                msg = "Please check your password"
                print(msg)
                context = {
                        "result"    : False,
                        "msg"       : msg
                        }
                return JsonResponse(context)
            
            # TEST Querry
            with conn:
                Querry = "select count(*) from APP_user "
                
                cur.execute(Querry)
                total = cur.fetchone()
                print('[TEST] Querry = '+Querry+' \n 총 수강생 수 : ',total[0])
                
            try :
                with conn:
                    Querry = " insert into APP_user \n"
                    Querry+= " (email, password, username, is_superuser, is_staff, is_active, date_joined) \n"
                    Querry+= " values ('"+email+"','"+password+"','"+username+"', '3', '3', '3', '"+currentTime+"') "
                    print(Querry)
                    cur.execute(Querry)
                    execute = cur.fetchone()
            except Exception as e:
                print('Exception : ',e)
                context = {"result" : False, "msg" : e}
                return JsonResponse(context,status = 400)
        
        context = {"result" : True}
        return JsonResponse(context,status=200)
    
    def login(request):
        conn = sqlite3.connect("db.sqlite3",check_same_thread=False)
        cur = conn.cursor()
        
        if request.method == 'POST':
            login_email     = request.POST.get("login_email");
            login_password  = request.POST.get("login_password");
            
            print("login_email",    login_email,    type(login_email))
            print("login_password", login_password, type(login_password))
            
            with conn:
                Querry = " SELECT * FROM APP_user WHERE email = '"+login_email+"'"

                print(Querry)
                cur.execute(Querry)
                password = cur.fetchone()
            
            print("password >>>>>>>>>>>",password)
            count = 0;
            # 1. 아이디 미입력 체크
            if login_email == None or login_email == "" :
                ++count
                print("# 1")
                msg = "아이디 미입력"
                context = {"result" : False, "msg" :msg}
                return JsonResponse(context,status = 200)
            
            # 2. 비밀번호 미입력 체크
            if login_password == None or login_password == "" :
                ++count
                print("# 2")
                msg = "비밀번호 미입력"
                context = {"result" : False, "msg" :msg}
                return JsonResponse(context,status = 200)
                
            # 3. 아이디 미등록 체크
            if password == None or password == "" :
                ++count
                print("# 3")
                msg = "아이디없음"
                context = {"result" : False, "msg" :msg}
                return JsonResponse(context,status = 200)
                
            # 4. 비밀번호가 맞지않음
            if login_password != password[1] :
                ++count
                print("# 4")  
                msg = "비밀번호 오류"
                context = {"result" : False, "msg" :msg}
                return JsonResponse(context,status=200)
            
            # 5. 로그인성공
            if count == 0 :
                print("# 5",count)   
                msg = "로그인 성공"
                context = {"result" : True, "msg" :msg}
                return JsonResponse(context,status = 200)