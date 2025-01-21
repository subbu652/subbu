from django.shortcuts import render,redirect
from todo.models import Task
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'homepage.html')

@login_required(login_url='signin')
def display(request):
    if request.method == "POST":
        item = request.POST.get('item')
        date = request.POST.get('date')
        Task.objects.create(title=item,due_date=date)
        return render(request,'todo_display.html',{"tasks":Task.objects.all()})
    data=Task.objects.all()
    return render(request,"todo_display.html",{'tasks':data})

@login_required(login_url='signin')
def edit(request,id):
    data=Task.objects.filter(id=id)
    if request.method == "POST":
        title = request.POST.get('item')
        status = request.POST.get('status')
        due_date = request.POST.get('date')
        data.update(title=title,status=status,due_date=due_date)
        return redirect('display')
    return render(request,'edit_form.html',{'data':data[0]})

@login_required(login_url='signin')
def remove(request,id):
    Task.objects.get(id=id).delete()
    return redirect('display')

@login_required(login_url='signin')
def finish(request,id):
    data=Task.objects.filter(id=id)
    data.update(status="Completed")
    return redirect('display')

def signup(request):
    if request.method == "POST":
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        mail = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        data = User.objects.filter(username=username)
        context = {"fname":fname, "lname":lname, "email":mail, "username":username}
        if data:
            messages.error(request, "Please use a different User Name")
            return render(request,'signup.html',context)
        if password == cpassword:
            User.objects.create_user(first_name=fname,last_name=lname,email=mail,username=username,password=password)
            messages.success(request,"The Record Added Successfully")
            return redirect('signin')
        messages.error(request,"Password doesn't match with Confirm Password")
        return render(request,'signup.html',context)
    return render(request,'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('display')
        messages.error(request,'Invalid Credentials')
        return redirect('signin')
    return render(request,'signin.html')

def signout(request):
    logout(request)
    return redirect('home')

def completed(request, inpt):
    return render(request,'todo_display.html',{'tasks':Task.objects.filter(status=inpt)})

def not_started(request,inpt):
    return render(request,'todo_display.html',{'tasks':Task.objects.filter(status=inpt)})

def started(request,inpt):
    return render(request,'todo_display.html',{'tasks':Task.objects.filter(status=inpt)})