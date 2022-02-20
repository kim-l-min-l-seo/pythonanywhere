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

### 2.3 가상환경 벗어나기

    deactivate

### 2.4 가상환경 장고 설치하기

    pip install django

### 2.6 pip 명령어 업데이트

    python -m pip install --upgrade pip

## 3. 프로젝트 생성

    mkdir WEB
    cd WEB

## 3.1 WEB 디렉터리를 프로젝트 디렉터리로 만들기
    
    django-admin startproject config . 