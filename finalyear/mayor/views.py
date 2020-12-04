from django.shortcuts import render, redirect

from accounts.models import Others
from public.models import HomeApplication,publicfeedback
from public.views import applyapplication
from officer.models import smsmayor
def mayorindex(request):
    obj = Others.objects.all()
    return  render( request,'mayor/mayorindex.html',{'other': obj})


def homeviewapplication(request):
    home=HomeApplication.objects.filter(PreviousTax='paid')
    context={
        'home':home,
    }
    return  render(request,'mayor/viewhomeapplication.html',context)

def delete(request, id):
    list = HomeApplication.objects.get(pk=id)
    list.delete()
    return redirect(homeviewapplication)

def officersms(request):
    sms=smsmayor.objects.all()
    context={
        'sms':sms
    }
    return render(request,'mayor/viewofficersms.html',context)


def delete1(request, id):
    list = smsmayor.objects.get(pk=id)
    list.delete()
    return redirect(officersms)

def ovijok(request):
    back=publicfeedback.objects.filter(throwby='mayor')
    context={
        'back':back
    }
    return  render(request,'mayor/publicovijok.html',context)

def deleteovijok(request,id):
    list = publicfeedback.objects.get(pk=id)
    list.delete()
    return redirect(ovijok)

