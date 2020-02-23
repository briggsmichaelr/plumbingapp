from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Report
from accounts.models import Userinfo


def home(request):
    return render(request,'diagnose/home.html')

def room(request):
    if request.method == "POST":
        report = Report()
        report.room = request.POST['room']
        report.save()
        return redirect('/diagnose/'+ str(report.id) + '/where/')
    else:
        return render(request, 'diagnose/room.html')


def where(request, report_id):
    report = get_object_or_404(Report, pk = report_id)
    if request.method == "POST":
        #render(request, 'diagnose/where.html')
        report.where = request.POST['where']
        report.save()
        return redirect('/diagnose/'+ str(report.id) + '/account/')
    elif report.room == 'Bathroom':
        return render(request, 'diagnose/where_bath.html')
    else:
        return render(request, 'diagnose/where_kitch.html')

def account(request, report_id):
    report = get_object_or_404(Report, pk = report_id)
    if request.method == "POST":
        #render(request, 'diagnose/where.html')
        if request.POST['account'] == 'No':
            return redirect('/accounts/'+ str(report.id) + '/signup/')
        else:
            return redirect('/accounts/'+ str(report.id) + '/login/')
    else:
        return render(request, 'diagnose/account.html')

def confirmation(request, report_id):
    report = get_object_or_404(Report, pk = report_id)
    userinfo = get_object_or_404(Userinfo, pk = report.user)
    return render(request, 'diagnose/confirmation.html', {'report':report, 'userinfo': userinfo})

def contractor(request):
    reports = Report.objects
    return render(request, 'diagnose/contractor.html', {'reports':reports})

def detail(request,report_id):
    report = get_object_or_404(Report, pk = report_id)
    userinfo = get_object_or_404(Userinfo, pk = report.user)
    return render(request, 'diagnose/detail.html', {'report':report, 'userinfo':userinfo})

def delete_report(DeleteView,report_id):
    reports = Report.objects
    reports.filter(pk=report_id).delete()
    return redirect('/contractor')
