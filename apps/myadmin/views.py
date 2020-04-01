from django.shortcuts import render
# Create your views here.
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import *
from django.http import JsonResponse
from django.views import generic
from django.http import HttpResponseRedirect
from django.views.generic import View
import os
import csv
import pandas as pd
BASE_DIR = os.getcwd()
# Create your views here.
def index(request):
    if request.method == 'GET':

        return render(request, 'myadmin.html')



def login(request):
    if request.method == 'POST':
        password=request.POST.get('password')
        with open("./static/9aoze2f2e0/password.txt","r") as f:
            lines=f.readlines()
            txtpassword=lines[0]
        if(password == txtpassword):

            data=[]
            content={}
            result=[]
            suggestion=[]

            file=open("./static/9aoze2f2e0/foreword.txt")
            lines=file.readlines()
            content['foreword']=lines[0]

            try:
                with open('./static/9aoze2f2e0/question.csv')as f:
                    f_csv = csv.reader(f)
                    for idx,row in enumerate(f_csv):
                        data.append(row)
                content['data']=data
            except:
                content['data']='请重新上传'
            try:
                with open('./static/9aoze2f2e0/suggestion.csv')as f:
                    f_csv = csv.reader(f)
                    for idx,row in enumerate(f_csv):
                        suggestion.append(row)
                content['suggestion']=suggestion
            except:
                content['suggestion']='请重新上传'

            try:
                with open('./static/9aoze2f2e0/result.csv')as f:
                    f_csv = csv.reader(f)
                    for idx,row in enumerate(f_csv):
                        result.append(row)
                content['result']=result
            except:
                content['result']='请重新上传'

            content['password'] = txtpassword

            return render(request, 'adminpage.html' ,{'content': content})
        else:
            return render(request, 'myadmin.html')
    else:
        return render(request, 'myadmin.html')

def upload(request,name):
    if request.method == 'POST':
        file = request.FILES.get(name,None)
        filename = name+'.csv'

        if not file:
            return render(request, 'myadmin.html')
        else:
            content={}
            if file.name != filename:
                return render(request, 'myadmin.html')
            else:

                f = open(os.path.join(BASE_DIR, 'static','9aoze2f2e0',filename), 'wb')
                for chunk in file.chunks():
                    f.write(chunk)
                    f.close()
                data=[]
                content={}
                result=[]
                suggestion=[]
                with open("./static/9aoze2f2e0/password.txt","r") as f:
                    lines=f.readlines()
                    txtpassword=lines[0]
                content['password'] = txtpassword
                file=open("./static/9aoze2f2e0/foreword.txt")
                lines=file.readlines()
                content['foreword']=lines[0]

                with open('./static/9aoze2f2e0/question.csv')as f:
                    f_csv = csv.reader(f)
                    for idx,row in enumerate(f_csv):
                        data.append(row)
                content['data']=data

                with open('./static/9aoze2f2e0/suggestion.csv')as f:
                    f_csv = csv.reader(f)
                    for idx,row in enumerate(f_csv):
                        suggestion.append(row)
                content['suggestion']=suggestion

                with open('./static/9aoze2f2e0/result.csv')as f:
                    f_csv = csv.reader(f)
                    for idx,row in enumerate(f_csv):
                        result.append(row)
                content['result']=result

                return render(request, 'adminpage.html',{'content': content})

def text(request):
    if request.method == 'POST':
        foreword=request.POST.get('foreword')
        with open("./static/9aoze2f2e0/foreword.txt","w") as f:
            f.writelines(foreword)
        data=[]
        content={}
        result=[]
        suggestion=[]

        with open("./static/9aoze2f2e0/password.txt","r") as f:
            lines=f.readlines()
            txtpassword=lines[0]
        content['password'] = txtpassword

        file=open("./static/9aoze2f2e0/foreword.txt")
        lines=file.readlines()
        content['foreword']=lines[0]

        with open('./static/9aoze2f2e0/question.csv')as f:
            f_csv = csv.reader(f)
            for idx,row in enumerate(f_csv):
                data.append(row)
        content['data']=data

        with open('./static/9aoze2f2e0/suggestion.csv')as f:
            f_csv = csv.reader(f)
            for idx,row in enumerate(f_csv):
                suggestion.append(row)
        content['suggestion']=suggestion

        with open('./static/9aoze2f2e0/result.csv')as f:
            f_csv = csv.reader(f)
            for idx,row in enumerate(f_csv):
                result.append(row)
        content['result']=result
        return render(request, 'adminpage.html' ,{'content': content})

    else:
        return render(request, 'myadmin.html')



def changepassword(request):
    if request.method == 'POST':
        password=request.POST.get('password')
        with open("./static/9aoze2f2e0/password.txt","w") as f:
            f.writelines(password)
        data=[]
        content={}
        result=[]
        suggestion=[]

        file=open("./static/9aoze2f2e0/foreword.txt")
        lines=file.readlines()
        content['foreword']=lines[0]

        with open('./static/9aoze2f2e0/question.csv')as f:
            f_csv = csv.reader(f)
            for idx,row in enumerate(f_csv):
                data.append(row)
        content['data']=data

        with open('./static/9aoze2f2e0/suggestion.csv')as f:
            f_csv = csv.reader(f)
            for idx,row in enumerate(f_csv):
                suggestion.append(row)
        content['suggestion']=suggestion

        with open('./static/9aoze2f2e0/result.csv')as f:
            f_csv = csv.reader(f)
            for idx,row in enumerate(f_csv):
                result.append(row)
        content['result']=result
        content['password'] = password

        return render(request, 'adminpage.html' ,{'content': content})

    else:
        return render(request, 'myadmin.html')
