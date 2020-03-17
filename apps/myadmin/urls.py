from django.conf.urls import include,url
from django.urls import path
from apps.myadmin.views import *
app_name = 'myadmin'

urlpatterns = [
    path('', index, name='index'),
    path('/login', login, name='login'),
    path('/upload/<name>', upload, name='upload'),
    path('/delete/<num>', delete, name='delete'),       
]
