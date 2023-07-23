from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import Profile
from . models import contactInformation
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'djangoapp/index.html');

@login_required
def index(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        pnumber = request.POST.get('pnumber')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        data = contactInformation(fname=fname, lname=lname, pnumber=pnumber, email=email, subject=subject)
        data.save()

        return render(request, 'siteapp\index.html')
    return render(request, 'siteapp\index.html');


@login_required
def company(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        pnumber = request.POST.get('pnumber')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        data = contactInformation(fname=fname, lname=lname, pnumber=pnumber, email=email, subject=subject)
        data.save()

        return render(request, 'siteapp\company.html')
    
    return render(request, 'siteapp\company.html');


@login_required
def services(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        pnumber = request.POST.get('pnumber')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        data = contactInformation(fname=fname, lname=lname, pnumber=pnumber, email=email, subject=subject)
        data.save()

        return render(request, 'siteapp\services.html')
    
    return render(request, 'siteapp\services.html');


@login_required
def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        pnumber = request.POST.get('pnumber')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        data = contactInformation(fname=fname, lname=lname, pnumber=pnumber, email=email, subject=subject)
        data.save()

        return render(request, 'siteapp\contact.html')
    
    return render(request, 'siteapp\contact.html');



def video(request):
    return render(request, 'siteapp\company.html');

@login_required
def table(request):
    datainfo = contactInformation.objects.all()
    context = {
        'datas' : datainfo
    }
    return render(request, 'siteapp/table.html', context) 


@login_required
def update(request, id):
    updateInformation = contactInformation.objects.get(id=id)
    if request.method =='POST':
        updateInformation.fname = request.POST.get('fname')
        updateInformation.lname = request.POST.get('lname')
        updateInformation.pnumber = request.POST.get('pnumber')
        updateInformation.email = request.POST.get('email')
        updateInformation.subject = request.POST.get('subject')
        updateInformation.save()
        
        return redirect('table')
    context = {
        'updated': updateInformation
    }
    return render(request, 'siteapp/update.html', context)



def clear(request, id):
    dels = contactInformation.objects.get(id=id)
    dels.delete()
    return redirect('table')


def user(request):
    return render(request, 'siteapp/user.html')