from ast import With
import filecmp
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from pytz import timezone
from oj.models import Problem,testcases,Submission
import datetime
import os, subprocess,chunk
from django.utils import timezone
from django.contrib.auth import authenticate, logout,login
def index(request):
    if request.user.is_anonymous:
        return redirect("/")
    problem_list= (Problem.objects.all())
    context= {'problem_list':problem_list}
    return render(request,'index.html',context)


def problem_desc(request,problem_id):
    problem= get_object_or_404(Problem,pk= problem_id)
    context= {'problem':problem}
    return render(request,'description.html',context)

def submit(request,problem_id):
    testcase= testcases.objects.get(pk=problem_id)
    with open(r'C:\Users\ACE\OneDrive\Desktop\Online_Judge_Project\Myproject\input.txt','w+') as input1:
        input1.write(testcase.input)
    with open(r'C:\Users\ACE\OneDrive\Desktop\Online_Judge_Project\Myproject\actual_output.txt','w+') as output1:
        output1.write(testcase.output)
    file= request.FILES['solution']
    
    with open(r'C:\Users\ACE\OneDrive\Desktop\Online_Judge_Project\Myproject\code.cpp','wb+') as cppfile:
        for chunk in file.chunks():
            cppfile.write(chunk)

    path= 'C:\\Users\\ACE\\OneDrive\\Desktop\\Online_Judge_Project\\Myproject'
    os.chdir(path)
    subprocess.call(['g++','code.cpp','-o','1.exe'],shell= True)
    subprocess.call('1.exe<input.txt>output.txt',shell=True)

    out1= r'C:\Users\ACE\OneDrive\Desktop\Online_Judge_Project\Myproject\output.txt'
    out2= r'C:\Users\ACE\OneDrive\Desktop\Online_Judge_Project\Myproject\actual_output.txt'

    if(filecmp.cmp(out1,out2,shallow=False)):
        verdict= "Correct answer"
    else:
        verdict= "Wrong answer"

    sol =Submission()
    sol.problem_id= Problem.objects.get(pk= problem_id)
    sol.verdict= verdict
    sol.submit_time= timezone.now()
    sol.save()
    return redirect("/judge")

def loginUser(request):
    if request.method =='POST':
        username =request.POST.get('username')
        password= request.POST.get("password")
        #check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            #a backend authenticated the credentials
            login(request, user)
            return redirect("judge")
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/")
    
# Create your views here.
