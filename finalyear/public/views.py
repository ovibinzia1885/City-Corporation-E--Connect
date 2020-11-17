from django.shortcuts import render, redirect
from .models import ApplyLicence

def publicindex(request):
    return render(request,'public/publicindex.html')

def addproblem(request):
    return render(request,'public/addproblem.html')
def applyapplication(request):
    return render(request,'public/applyapplication.html')


def applylicence(request):
    current = request.user
    if request.method == "POST":
        # name = request.POST[' name']
        FatherName = request.POST['FatherName']
        NIDNumber = request.POST['NIDNumber']

        type = request.POST['type']
        address = request.POST['address']
        price = request.POST['price']
        ward = request.POST['ward']
        pyment = request.POST['pyment']
        licence=ApplyLicence(name=current,FatherName=FatherName,NIDNumber=NIDNumber,type=type,address=address,price=price,ward=ward,pyment=pyment)
        licence.save()

    return render(request,'public/applylicence.html')


def viewapplylicenece(request):
    licence = ApplyLicence.objects.all()
    context = {
        'licence':licence,
    }
    return render(request,'public/viewapplylicence.html', context)


def onlinebirthcertificate(request):
    return render(request,'public/onlinebirthcertificate.html')


def GivenHomeTax(request):
    return render(request,'public/giventax.html')


def FeedBack(request):
    return render(request,'public/feedback.html')
def edit(request,id):
    license=ApplyLicence.objects.get(pk=id)
    context={
        'licence':license
    }
    return render(request, 'public/editlicence.html', context)
def update(request,id=None):
    if request.method=="POST":
        if id is not None:
            license=ApplyLicence.objects.get(id=id)
            # name = request.POST[' name']
            license.FatherName = request.POST['FatherName']
            license.NIDNumber = request.POST['NIDNumber']

            license.type = request.POST['type']
            license.address = request.POST['address']
            license.price = request.POST['price']
            license.ward = request.POST['ward']
            license.pyment = request.POST['pyment']
            license.save()

    return redirect(viewapplylicenece)
def delete(request, id):
    list = ApplyLicence.objects.get(pk=id)
    list.delete()
    return redirect(viewapplylicenece)
