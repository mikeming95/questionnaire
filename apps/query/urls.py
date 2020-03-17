from django.conf.urls import include,url
from django.urls import path
from apps.query.views import *
app_name = 'query'

urlpatterns = [

    path('result', result, name='result'),

]
