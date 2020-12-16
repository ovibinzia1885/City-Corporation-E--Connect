from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.urls import reverse
from django.contrib.auth.models import User

from accounts.models import Others
from .models import ApplyLicence, HomeApplication, HomeTax, Onlinebdapply, Addproblem,publicfeedback

def publicindex(request):
    if request.session.get('public_username'):
        print(request.session.get('public_username'))
        obj = Others.objects.all()
        return render(request, 'public/publicindex.html', {'other': obj})
    else:
        return redirect('login')

def addproblem(request):
    current = request.user
    if request.method == "POST":
        ProblemType = request.POST['ProblemType']
        WardNo = request.POST['WardNo']
        Address = request.POST['Address']
        Breif = request.POST['Breif']
        ProblemPicture = request.POST['ProblemPicture']
        problem = Addproblem(name=current, ProblemType=ProblemType, WardNo=WardNo, Address=Address, Breif=Breif,
                             ProblemPicture=ProblemPicture)
        problem.save()
        # if WardNo == '1':
        #     return render(request, 'officer/wardno_1.html')
        # elif WardNo == '2':
        #     return render(request, 'officer/wardno_2.html')
        # elif WardNo == '3':
        #     return render(request, 'officer/wardno_3.html')

    return render(request, 'public/addproblem.html')


def applyapplication(request):
    current = request.user
    if request.method == "POST":
        FatherName = request.POST['FatherName']
        wardno = request.POST['wardno']
        address = request.POST['address']
        NIDNumber = request.POST['NIDNumber']
        HondingNo = request.POST['HondingNo']
        PreviousTax = request.POST['PreviousTax']
        SelectFloor = request.POST['SelectFloor']
        pic = request.POST['pic']
        payment = request.POST['payment']
        homeapplication = HomeApplication(name=current, FatherName=FatherName, wardno=wardno, address=address,
                                          NIDNumber=NIDNumber, HondingNo=HondingNo, PreviousTax=PreviousTax,
                                          SelectFloor=SelectFloor, pic=pic, payment=payment)
        homeapplication.save()

    return render(request, 'public/applyapplication.html')


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
        licence = ApplyLicence(name=current, FatherName=FatherName, NIDNumber=NIDNumber, type=type, address=address,
                               price=price, ward=ward, pyment=pyment)
        licence.save()

    return render(request, 'public/applylicence.html')


def viewapplylicenece(request):
    licence = ApplyLicence.objects.all()
    context = {
        'licence': licence,
    }
    return render(request, 'public/viewapplylicence.html', context)


def onlinebirthcertificate(request):
    current = request.user
    if request.method == "POST":
        PersonalNumber = request.POST['PersonalNumber']
        FatherName = request.POST['FatherName']
        MotherName = request.POST['MotherName']
        BithofDate = request.POST['BithofDate']
        PresentAddress = request.POST['PresentAddress']
        Gender = request.POST['Gender']
        subdistict = request.POST['subdistict']
        oldpic = request.POST['oldpic']
        certificate = Onlinebdapply(name=current, PersonalNumber=PersonalNumber, FatherName=FatherName,
                                    MotherName=MotherName, BithofDate=BithofDate, PresentAddress=PresentAddress,
                                    Gender=Gender, subdistict=subdistict, oldpic=oldpic)
        certificate.save()
    return render(request, 'public/onlinebirthcertificate.html')


def GivenHomeTax(request):
    current = request.user
    if request.method == "POST":
        ward_no = request.POST['ward_no']
        HoldingNo = request.POST['HoldingNo']
        taxyear = request.POST['taxyear']
        TaxType = request.POST['TaxType']
        price = request.POST['price']
        pictureowner = request.POST['pictureowner']
        payment = request.POST['payment']
        tax = HomeTax(name=current, ward_no=ward_no, HoldingNo=HoldingNo, taxyear=taxyear, TaxType=TaxType, price=price,
                      pictureowner=pictureowner, payment=payment)
        tax.save()

    return render(request, 'public/giventax.html')


def sentfeedback(request):
    current=request.user
    if request.method=="POST":
        throwby=request.POST['throwby']
        problemtype=request.POST['problemtype']
        description=request.POST['description']
        result=publicfeedback(name=current,throwby=throwby,problemtype=problemtype,description=description)
        result.save()

    return render(request, 'public/feedback.html')


def edit(request, id):
    license = ApplyLicence.objects.get(pk=id)
    context = {
        'license': license
    }
    return render(request, 'public/editlicence.html', context)


def update(request, id=None):
    if request.method == "POST":
        if id is not None:
            license = ApplyLicence.objects.get(id=id)
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


def deshbord(request):
    counterproblem = 0
    counterapplication = 0
    license = 0
    licencecost = 0
    bdcertificateapply = 0
    applytax = 0
    totaltax = 0
    taxyear1 = ''
    problem = Addproblem.objects.all()
    application = HomeApplication.objects.all()
    licence = ApplyLicence.objects.all()
    bdcertificate = Onlinebdapply.objects.all()
    ovi = HomeTax.objects.all()
    for i in problem:
        counterproblem += 1

    for i in application:
        counterapplication += 1
        print(counterapplication)

    for i in licence:
        license += 1
        licencecost += int(i.price)
        print(licencecost)
    for i in bdcertificate:
        bdcertificateapply += 1
        print(bdcertificateapply)

    for i in ovi:
        applytax += 1
        totaltax += int(i.price)
        taxyear1 += i.taxyear + ","
        print(totaltax)
        print(taxyear1)

    return render(request, 'public/deshbord.html', {'counterproblem': counterproblem, 'counterapplication': counterapplication, 'license': license, 'bdcertificateapply': bdcertificateapply, 'taxyear1': taxyear1, 'licencecost': licencecost, 'totaltax': totaltax})


def logout(request):
	if request.method=="POST":
         auth.logout(request)
         del request.session['public_username']
	return HttpResponseRedirect(reverse('index'))