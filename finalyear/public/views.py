from django.shortcuts import render

def publicindex(request):
    return render(request,'public/publicindex.html')

def addproblem(request):
    return render(request,'public/addproblem.html')
def applyapplication(request):
    return render(request,'public/applyapplication.html')
def applylicence(request):
    return render(request,'public/applylicence.html')
def onlinebirthcertificate(request):
    return render(request,'public/onlinebirthcertificate.html')
def GivenHomeTax(request):
    return render(request,'public/giventax.html')
def FeedBack(request):
    return render(request,'public/feedback.html')