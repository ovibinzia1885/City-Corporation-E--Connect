from django.shortcuts import render

def mayorindex(request):
    return  render( request,'mayor/mayorindex.html')