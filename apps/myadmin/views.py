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
        if(password=='123'):
            data=[]
            content={}
            record=[]
            suggestion=[]
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

            with open('./static/9aoze2f2e0/record.csv')as f:
                f_csv = csv.reader(f)
                for idx,row in enumerate(f_csv):
                    record.append(row)
            content['record']=record

            return render(request, 'adminpage.html' ,{'content': content})
        else:
            return render(request, 'myadmin.html')
    else:
        return render(request, 'myadmin.html')

def upload(request,name):
    if request.method == 'POST':
        file = request.FILES.get(name,None)
        filename = name+'.csv'
        print(filename)
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
                record=[]
                suggestion=[]
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

                with open('./static/9aoze2f2e0/record.csv')as f:
                    f_csv = csv.reader(f)
                    for idx,row in enumerate(f_csv):
                        record.append(row)
                content['record']=record

                return render(request, 'adminpage.html',{'content': content})

def delete(request,num):
    if request.method == 'GET':

        df=pd.read_csv('./static/9aoze2f2e0/record.csv',encoding="gbk")

        df.drop(df.index[int(num)-2],inplace=True)
        #print(df.head())
        df.to_csv('./static/9aoze2f2e0/record.csv',index=None)
        data=[]
        content={}
        record=[]
        suggestion=[]
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

        with open('./static/9aoze2f2e0/record.csv')as f:
            f_csv = csv.reader(f)
            for idx,row in enumerate(f_csv):
                record.append(row)
        content['record']=record

        return render(request, 'adminpage.html' ,{'content': content})
