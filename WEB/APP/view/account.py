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
                Querry = "select count(*) from auth_user "
                
                cur.execute(Querry)
                total = cur.fetchone()
                print('[ TEST ] Querry = '+Querry+' \n 총 수강생 수 : ',total[0])
                
            try :
                with conn:
                    Querry = " insert into auth_user \n"
                    Querry+= " (email, password, username, is_superuser, is_staff, is_active, date_joined, first_name, last_name) \n"
                    Querry+= " values ('"+email+"','"+password+"','"+username+"', '3', '미사용컬럼', '미사용컬럼', '"+currentTime+"', '미사용컬럼', '미사용컬럼') "
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
        
        if request.method == 'POST':
            login_email     = request.POST.get("login_email");
            login_password  = request.POST.get("login_password");
            
            print("login_email",    login_email,    type(login_email))
            print("login_password", login_password, type(login_password))
            
            from pathlib import Path
            print("BASEDIR ::",Path(__file__).resolve().parent.parent)
            
            conn = sqlite3.connect("db.sqlite3",check_same_thread=False)
            cur = conn.cursor()
            
            print("conn ::",conn)
            print("cur  ::",cur)
                
            with conn:
                Querry = " SELECT * FROM auth_user WHERE email = '"+login_email+"'"

                print(Querry)
                cur.execute(Querry)
                member = cur.fetchone()
            
            print("member >>>>>>>>>>>",member)
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
            if member == None or member == "" :
                ++count
                print("# 3")
                msg = "아이디없음"
                context = {"result" : False, "msg" :msg}
                return JsonResponse(context,status = 200)
                
            # 4. 비밀번호가 맞지않음
            if login_password != member[1] :
                ++count
                print("# 4")  
                msg = "비밀번호 오류"
                context = {"result" : False, "msg" :msg}
                return JsonResponse(context,status=200)
            
            # 5. 로그인성공
            if count == 0 :
                print("# 5",count)   
                msg = "로그인 성공"
                
                request.session['id']           = member[0]
                request.session['password']     = member[1]
                request.session['last_login']   = member[2]
                request.session['is_superuser'] = member[3]
                request.session['username']     = member[4]
                request.session['first_name']   = member[5]
                request.session['last_name']    = member[6]
                request.session['is_staff']     = member[7]
                request.session['is_active']    = member[8]
                request.session['date_joined']  = member[9]
                request.session['email']        = member[10]

                print("session",request.session.session_key)
                context = {"result" : True, 
                           "msg" :msg}
                
                return JsonResponse(context,status = 200)
                # return redirect('/BLACKCODE/XX11/0000/XX')
            
    def logout(request):
        # del request.session['id']
        request.session.pop('id')
        
        request.session.flush()

        url = 'BLACKCODE'
        web = 'XX11'
        ver = 'VER 1.0.0'
        context = {
                'url'   : url, 
                'title' : '',
                'ver'   : ver
            }
        # return render(request, './'+url+'/'+web+'/0000_index.html', context)
        # return HttpResponse("You're logged out.")
        return redirect('/BLACKCODE/XX11/0000/XX')