from django.shortcuts import render, redirect

from public.models import ApplyLicence
from public.views import viewapplylicenece


def officerindex(request):
    return  render(request,'officer/officerindex.html')

def councilordetlis(request):
    return render(request,'officer/councilordetlies.html')
def taxview(request):
    return render(request,'officer/taxcheek.html')
def viewcertificate(request):
    return render(request,'officer/viewbirthcertificate.html')
def licenceview(request):
    return render(request,'officer/viewlicencen.html')
def viewproblem(request):
    return render(request,'officer/viewproblem.html')
def workshop(request):
    return render(request,'officer/workshop.html')


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