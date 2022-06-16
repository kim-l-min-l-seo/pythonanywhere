from django.shortcuts import render
# from pytube import YouTube
from django.core.files.storage import FileSystemStorage
import os
from tkinter import filedialog
from tkinter import *
# 특정영상 다운로드

def down(request, menu, url):
    print("menu : ",menu)
    print("url : ",url)
    
    if request.method == 'POST':
        
        dataUrl = request.POST.get('dataUrl')
        print(dataUrl)
        
        # yt = YouTube(dataUrl)
        # yt.streams.filter(only_audio=True).first().download()

    
        context = { 'vids': ""}
        return render(request, './web/game/index.html', context)
    
def downVideo(request,url):
    # YouTube(url).streams.first().download()
    pass
    
def downMusic(request, url):
    # yt = YouTube('https://www.youtube.com/watch?v=...')

    # print(yt.streams.filter(only_audio=True).all())
    # 특정영상 다운로드
    # yt.streams.filter(only_audio=True).first().download()

    print('success')