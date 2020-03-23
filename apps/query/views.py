from django.shortcuts import *
from django.views.generic import View
from django.shortcuts import render,render_to_response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import generic
import pandas as pd
import json
import time
import csv
# Create your views here.


class Index(View):
    def get(self, request):
        df=pd.read_csv('static/9aoze2f2e0/question.csv',encoding='gbk')
        col = [column for column in df]
        num = max(list(df['id']))  #max id
        ddict={}
        content2={}
        file=open("./static/9aoze2f2e0/foreword.txt")
        lines=file.readlines()
        content2['foreword']=lines[0]

        for j in range(num):
            choice=[]
            for i in range(2,len(col)-1,2):
                choice.append(df.iloc[j][col[i]])

            ddict[df.iloc[j]['id']]={'id':df.iloc[j]['id'],'content':df.iloc[j][1],'choice':choice}


        return render_to_response("web.html",{'content': ddict,'content2':content2})

def result(request):
    if request.method == 'POST':
        content={}
        answer=[]
        summ=0
        df=pd.read_csv('static/9aoze2f2e0/question.csv',encoding='gbk')
        col = [column for column in df]
        num = max(list(df['id']))  #max id
        for j in range(num):
            re_=[]
            for i in range(3,len(col),2):
                re_.append(df.iloc[j][col[i]])
            summ=summ+re_[int(request.POST.get(('q'+str(j+1))))-1]

        username=request.POST.get('username')
        userphone=request.POST.get('userphone')
        usercompany=request.POST.get('usercompany')
        countryCode=request.POST.get('countryCode')

        print(countryCode)

        localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        path  = "static/9aoze2f2e0/result.csv"


        with open(path, 'a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow([username,countryCode+userphone,usercompany,summ,localtime])


        su=pd.read_csv('static/9aoze2f2e0/suggestion.csv',encoding='gbk')

        score=list(su['score'])
        try:
            for idx,item in enumerate(score):
                if(summ<item):
                    content['suggestion']=su['suggestion'][idx]
                    break
        except:
            content['suggestion']=''

        content['sum']=summ

        return render(request, 'result.html', {'content': content})
