from django.shortcuts import render, redirect
from public.models import HomeApplication
from public.views import applyapplication
def mayorindex(request):
    return  render( request,'mayor/mayorindex.html')


def homeviewapplication(request):
    home=HomeApplication.objects.filter(PreviousTax='paid')
    context={
        'home':home,
    }
    return  render(request,'mayor/viewhomeapplication.html',context)

def delete(request, id):
    list = HomeApplication.objects.get(pk=id)
    list.delete()
    return redirect(homeviewapplication)

