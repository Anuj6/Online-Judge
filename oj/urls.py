from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from oj import views
from oj.models import Problem
app_name='oj'
urlpatterns = [
    path('',views.index,name='problems'),
    path('problem/<int:problem_id>/',views.problem_desc, name= 'problem_desc'),
    path('problem/<int:problem_id>/submit/',views.submit, name= 'submit'),
]