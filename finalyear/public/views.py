from django.shortcuts import render

def publicindex(request):
    return render(request,'public/publicindex.html')

def addproblem(request):
    return render(request,'public/addproblem.html')