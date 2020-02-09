from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request,report_id):
    #if report_id != '1':
    if request.method == 'POST':
        #user has info
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken dumby!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                auth.login(request, user)
                if report_id != '1':
                    return redirect('/diagnose/'+ str(report_id) + '/confirmation/')
                else:
                    return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Ahhh! Passwords muct match!!!'})
    else:
        #user wants to input info
        return render(request, 'accounts/signup.html')
        

def login(request):
    if request.method == 'POST':
        #user has info
        user = auth.authenticate(username=request.POST.get('username'), password = request.POST.get('password'))
        if user is None:
            return render(request, 'accounts/login.html', {'error':'Ahhh! Password or Username is Incorrect!!!'})
        else:
            auth.login(request, user)
            return redirect('home')
    else:
        #user wants to input info
        return render(request, 'accounts/login.html')

def logout(request):
    #if request.method == 'POST':
    auth.logout(request)
    return redirect('home')
# Create your views here.
