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
        return render_to_response("index.html")


class questionairepage(View):
    def post(self, request):
        username=request.POST.get('username')
        usercompany=request.POST.get('usercompany')
        userphone=request.POST.get('userphone')

        if(len(userphone)>10):
            userphone = '86' + userphone
        else:
            userphone = '852' + userphone

        df=pd.read_csv('static/9aoze2f2e0/question.csv',encoding='gbk')
        col = [column for column in df]
        num = max(list(df['id']))  #max id
        ddict={}
        content2={}
        file=open("./static/9aoze2f2e0/foreword.txt")
        lines=file.readlines()
        content2['foreword']=lines[0]
        content2['num']=num
        for j in range(num):
            choice=[]
            for i in range(2,len(col)-1,2):
                if(df.iloc[j][col[i]]== 'na' ):
                    pass
                else:
                    choice.append(df.iloc[j][col[i]])

            ddict[df.iloc[j]['id']]={'id':df.iloc[j]['id'],'content':df.iloc[j][1],'choice':choice}
        response = render_to_response("web.html",{'content': ddict,'content2':content2})
        response.set_cookie('username',username)
        response.set_cookie('usercompany',usercompany)
        response.set_cookie('userphone',userphone)
        return response

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

            exec('q_%d = %d' % (j+1 ,int(request.POST.get(('q'+str(j+1))))) )

        value=[]
        index=[]
        for i in range(num):
            exec('value.append(q_%d)' % (i+1) )
            exec("index.append('q_%d')" % (i+1) )


        username=request.COOKIES.get('username')
        userphone=request.COOKIES.get('userphone')
        usercompany=request.COOKIES.get('usercompany')

        localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        path  = "static/9aoze2f2e0/result.csv"
        code=[username,userphone,usercompany,summ,localtime]+value

        datarecord=[]
        with open(path,'r')as f:
            f_csv = csv.reader(f)
            for idx,row in enumerate(f_csv):
                if(idx==0):
                    datarecord.append(['username','phone','usercompany','summ','localtime']+index)
                else:
                    datarecord.append(row)

        with open(path, 'w',newline='') as f:
            for i in datarecord:
                writer = csv.writer(f)
                writer.writerow(i)


        with open(path, 'a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(code)


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
