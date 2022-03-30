from django.shortcuts import render,redirect
from django .http import HttpResponse
from .models import student,login1

# Create your views here.
def display(request):
    return render(request,'login.html')
def post(request):
    a = request.POST['n1']
    b = request.POST['n2']
    c = request.POST['n3']
    u = request.POST['s1']
    p = request.POST['s2']
    data = student(rollno=a,name=b,age=c,username=u,password=p)
    data.save()
    data1 = login1(username=u,password=p)
    data1.save()
    return HttpResponse("success")
"""def logs(request):
        if request.method=='POST':
            u = request.POST['n4']
            p = request.POST['n5']
            data = login1.objects.get(username=u)
            if data.password == p:
               request.session['id']=u
                return redirect(home)
        else:
             return HttpResponse("invalid")
    return render(re)
def find(request):
    if request.method=='POST':
        p = request.post['n1']"""
