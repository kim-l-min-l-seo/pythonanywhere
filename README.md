# Pythonanywhere를 이용한 Python Web Project 배포

## 개발환경

    os : windows 10
    language : python

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