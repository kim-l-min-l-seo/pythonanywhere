# Pythonanywhere를 이용한 Python Web Project 배포

## 개발환경

    os : windows 10
    language : python
    배포툴 : https://www.pythonanywhere.com/
    배포 url : http://iiblackcode.pythonanywhere.com/

## 1. GIT 연결/연동

    git init
    git remote add origin https://github.com/IIBlackCode/pythonanywhere.git
    git pull origin master

## 2. 가상환경

### 2.1 가상환경 생성

    python -m venv venv

### 2.2 가상환경 진입

    cd .\venv\Scripts\
    .\activate

-------------------------------------------------------------------

### 2.2 ex)

    PS F:\BlackCode\PYTHON\WODKSPACE\Pythonanywhere> python -m venv venv
    PS F:\BlackCode\PYTHON\WODKSPACE\Pythonanywhere> cd .\venv\Scripts\  
    PS F:\BlackCode\PYTHON\WODKSPACE\Pythonanywhere\venv\Scripts> .\activate
    (venv) PS F:\BlackCode\PYTHON\WODKSPACE\Pythonanywhere\venv\Scripts> 

### 2.3 가상환경 벗어나기

    deactivate

-------------------------------------------------------------------

### 2.3 ex)

    (venv) PS F:\BlackCode\PYTHON\WODKSPACE\Pythonanywhere\venv\Scripts> deactivate      
    PS F:\BlackCode\PYTHON\WODKSPACE\Pythonanywhere\venv\Scripts> 

### 2.4 가상환경 장고 설치하기

    pip install django

    -------------------------------------------------------------------

    (venv) PS F:\BlackCode\PYTHON\WODKSPACE\Pythonanywhere> pip install django
    Collecting django
    Downloading Django-3.2.12-py3-none-any.whl (7.9 MB)
        |████████████████████████████████| 7.9 MB 6.8 MB/s
    Collecting sqlparse>=0.2.2
    Using cached sqlparse-0.4.2-py3-none-any.whl (42 kB)
    Collecting asgiref<4,>=3.3.2
    Downloading asgiref-3.5.0-py3-none-any.whl (22 kB)
    Collecting pytz
    Using cached pytz-2021.3-py2.py3-none-any.whl (503 kB)
    Collecting typing-extensions; python_version < "3.8"
    Downloading typing_extensions-4.1.1-py3-none-any.whl (26 kB)
    Installing collected packages: sqlparse, typing-extensions, asgiref, pytz, django
    Successfully installed asgiref-3.5.0 django-3.2.12 pytz-2021.3 sqlparse-0.4.2 typing-extensions-4.1.1
    WARNING: You are using pip version 20.1.1; however, version 22.0.3 is available.
    You should consider upgrading via the 'f:\blackcode\python\wodkspace\pythonanywhere\venv\scripts\python.exe -m pip install --upgrade pip' command.

### 2.6 pip 명령어 업데이트

    python -m pip install --upgrade pip

    -------------------------------------------------------------------

    Collecting pip
    Downloading pip-22.0.3-py3-none-any.whl (2.1 MB)
        |████████████████████████████████| 2.1 MB 6.4 MB/s
    Installing collected packages: pip
    Attempting uninstall: pip
        Found existing installation: pip 20.1.1
        Uninstalling pip-20.1.1:
        Successfully uninstalled pip-20.1.1
    Successfully installed pip-22.0.3

## 3. 프로젝트 생성

    mkdir WEB
    cd WEB

## 3.1 WEB 디렉터리를 프로젝트 디렉터리로 만들기
    
    django-admin startproject config . 

    -------------------------------------------------------------------

    (venv) PS F:\BlackCode\PYTHON\WODKSPACE\Pythonanywhere> cd .\WEB\
    (venv) PS F:\BlackCode\PYTHON\WODKSPACE\Pythonanywhere\WEB> django-admin startproject config .