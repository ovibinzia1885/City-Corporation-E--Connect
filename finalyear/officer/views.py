from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

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

# def officerviewapplylicenece(request):
#     licence = ApplyLicence.objects.all()
#     page = request.GET.get('page', 1)
#     paginator = Paginator(licence, 2)
#     try:
#         licence = paginator.page(page)
#     except PageNotAnInteger:
#         # fallback to the first page
#         licence = paginator.page(1)
#     except EmptyPage:
#         # probably the user tried to add a page number
#         # in the url, so we fallback to the last page
#         licence = paginator.page(paginator.num_pages)
#     context = {
#         'licence':licence,
#     }
#     return render(request,'officer/viewapplylicence.html', context)

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