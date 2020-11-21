from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from public.models import ApplyLicence,HomeTax,Onlinebdapply,Addproblem
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
    listing_list = Onlinebdapply.objects.all()

    paginator = Paginator(listing_list, 1)
    page = request.GET.get('page', 1)
    try:
        certificate = paginator.page(page)
    except PageNotAnInteger:
        # fallback to the first page
        certificate = paginator.page(1)
    except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
        certificate = paginator.page(paginator.num_pages)

    context = {
        'certificate': certificate,
    }
    return render(request, 'officer/viewbirthcertificate.html', context)

def licenceview(request):
    return render(request,'officer/viewlicencen.html')
def viewproblem(request):
    return render(request,'officer/viewproblem.html')
def workshop(request):

    return render(request,'officer/workshop.html')
def Smsmayor(request):
    return render(request,'officer/mayor.html')

def wardno1(request):

    problem=Addproblem.objects.filter(WardNo='1')
    context={
        problem:'problem'
    }
    return render(request,'officer/wardno_1.html',context)
def wardno2(request):
    return render(request,'officer/wardno_2.html')
def wardno3(request):
    return render(request,'officer/wardno_3.html')


def officerviewapplylicenece(request):
    licence_list = ApplyLicence.objects.all()
    page = request.GET.get('page', 3)

    paginator = Paginator(licence_list, 1)
    try:
        licence = paginator.page(page)
    except PageNotAnInteger:
        licence = paginator.page(1)
    except EmptyPage:
        licence = paginator.page(paginator.num_pages)

    return render(request, 'officer/viewapplylicence.html', { 'licence': licence })


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