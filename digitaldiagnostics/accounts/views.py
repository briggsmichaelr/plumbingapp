from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Userinfo

from diagnose.models import Report

def signup(request,report_id):
    #if report_id != '1':
    if request.method == 'POST':
        #user has info
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['email'])
                return render(request, 'accounts/signup.html', {'error':'Email has already been taken dumby!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['email'], password = request.POST['password1'])
                auth.login(request, user)
                if report_id != '1':
                    userinfo = Userinfo()
                    userinfo.phone = request.POST['phone']
                    userinfo.name = request.POST['name']
                    userinfo.email = request.POST['email']
                    userinfo.address1 = request.POST['address1']
                    userinfo.address2 = request.POST['address2']
                    userinfo.city = request.POST['city']
                    userinfo.state = request.POST['state']
                    userinfo.zip_code = request.POST['zip_code']
                    report = get_object_or_404(Report, pk = report_id)
                    report.user = userinfo.email
                    userinfo.save()
                    report.save()
                    return redirect('/diagnose/'+ str(report_id) + '/confirmation/')
                else:
                    return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Ahhh! Passwords muct match!!!'})
    else:
        #user wants to input info
        return render(request, 'accounts/signup.html')


def login(request,report_id):
    if request.method == 'POST':
        #user has info
        user = auth.authenticate(username=request.POST.get('email'), password = request.POST.get('password'))
        if user is None:
            return render(request, 'accounts/login.html', {'error':'Ahhh! Password or Email is Incorrect!!!'})
        else:
            auth.login(request, user)
            if report_id != '1':
                userinfo = get_object_or_404(Userinfo, pk = request.POST['email'])
                report = get_object_or_404(Report, pk = report_id)
                report.user = userinfo.email
                userinfo.save()
                report.save()
                return redirect('/diagnose/'+ str(report_id) + '/confirmation/')
            else:
                return redirect('home')
    else:
        #user wants to input info
        return render(request, 'accounts/login.html')

def logout(request):
    #if request.method == 'POST':
    auth.logout(request)
    return redirect('home')

# Create your views here.
