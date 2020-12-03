from django.shortcuts import render, redirect

from accounts.models import Others
from public.models import HomeApplication
from public.views import applyapplication
def mayorindex(request):
    obj = Others.objects.all()
    return  render( request,'mayor/mayorindex.html',{'other': obj})


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

