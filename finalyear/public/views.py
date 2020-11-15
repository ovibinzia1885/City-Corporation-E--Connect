from django.shortcuts import render

def publicindex(request):
    return render(request,'public/publicindex.html')

def addprobelm(request):
    return render(request,'public/addproblem.html')