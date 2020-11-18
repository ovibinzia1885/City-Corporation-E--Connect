from django.shortcuts import render

def mayorindex(request):
    return  render( request,'mayor/mayorindex.html')

def homeviewapplication(request):
    return  render(request,'mayor/viewhomeapplication.html')