from django.shortcuts import render

def officerindex(request):
    return  render(request,'officer/officerindex.html')
