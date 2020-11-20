from django.shortcuts import render, redirect

from public.models import ApplyLicence,HomeTax,Onlinebdapply
from public.views import viewapplylicenece


def officerindex(request):
    return  render(request,'officer/officerindex.html')

def Feedback(request):
    return render(request,'officer/councilordetlies.html')
def taxview(request):
    tax=HomeTax.objects.all()
    contex={
        'tax':tax
    }
    return render(request,'officer/taxcheek.html',contex)
def viewcertificate(request):
    certificate=Onlinebdapply.objects.all()
    context={
        'certificate':certificate
    }
    return render(request,'officer/viewbirthcertificate.html',context)
def licenceview(request):
    return render(request,'officer/viewlicencen.html')
def viewproblem(request):
    return render(request,'officer/viewproblem.html')
def workshop(request):
    return render(request,'officer/workshop.html')
def Smsmayor(request):
    return render(request,'officer/mayor.html')

def officerviewapplylicenece(request):
    licence = ApplyLicence.objects.all()
    context = {
        'licence':licence,
    }
    return render(request,'officer/viewapplylicence.html', context)

def delete(request, id):
    list = ApplyLicence.objects.get(pk=id)
    list.delete()
    return redirect(viewapplylicenece)
def delete1(request, id):
    list = Onlinebdapply.objects.get(pk=id)
    list.delete()
    return redirect(viewcertificate)
def delete2(request, id):
    list = HomeTax.objects.get(pk=id)
    list.delete()
    return redirect(taxview)