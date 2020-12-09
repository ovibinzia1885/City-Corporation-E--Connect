import os

from django.conf import settings
from django.template.loader import get_template
from django.views.generic import ListView
from xhtml2pdf import pisa
from django.contrib import messages, auth
from django.urls import reverse
from django.contrib.auth.models import User
from mayor.models import FileAdmin
from officer.models import uploadbudget,FileAdmin,OnlineBd,notice
from .models import Others,School,FamousPlace,hotline,recentlysolveproblem,councilorinfromation

from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from userprofile.models import UserRole


def index(request):
    print(5)
    obj = Others.objects.all()
    print(5)

    return render(request, 'accounts/index.html', {'other': obj})

def registration(request):
    if request.method == "POST":
        method_dict = request.POST.copy()
        first_name = method_dict.get('first_name')
        usertype = method_dict.get('usertype')
        last_name = method_dict.get('last_name')
        username = method_dict.get('username')
        email = method_dict.get('email')
        password = method_dict.get('password')
        password2 = method_dict.get('password2')
        # WardNo = method_dict.get('WardNo')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exist!')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already taken!')
                else:
                    user = User.objects.create_user(username=username,
                                                    password=password,
                                                    first_name=first_name,
                                                    last_name=last_name,
                                                    email=email
                                                    )
                    UserRole.objects.create(user=user, role=usertype, )
                    messages.success(request, 'You are successfully registered!')
                    return HttpResponseRedirect(reverse('login'))
        else:
            messages.error(request, 'Password does not match!')

        return HttpResponseRedirect(reverse('registration'))

    #	return redirect('user-register') # not standard

    return render(request, 'accounts/registration.html')


def login(request):
    if request.method == "POST":
        method_dict = request.POST.copy()
        username = method_dict.get('username')
        password = method_dict.get('password')

        user = auth.authenticate(username=username, password=password, )

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are successfully logged in!')
            # return HttpResponseRedirect(reverse('index'))
            if request.user.userrole.role == 'mayor':
                return render(request, 'mayor/mayorindex.html')
            elif request.user.userrole.role == 'officer':
                return render(request, 'officer/officerindex.html')
            elif request.user.userrole.role == 'public':
                return render(request, 'public/publicindex.html')
        else:
            messages.error(request, 'Invalid Credentials!')
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'accounts/login.html')


def solveproblem(request):
    solvelist = recentlysolveproblem.objects.all()
    context = {
        'solvelist': solvelist
    }
    return render(request, 'accounts/solveproblem.html',context)


def permissionletter(request):
    context = {'file': FileAdmin.objects.all()}
    return render(request, 'accounts/permiisionletter.html', context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response

    raise Http404


def schoolcollege(request):
    listing_list = School.objects.all()
    context = {
        'listing_list': listing_list
    }
    return render(request, 'accounts/schoolcollege.html',context)


def officernotice(request):
    note=notice.objects.all()
    context={
        'note':note
    }
    return render(request, 'accounts/notice.html',context)


def number(request):

    list=hotline.objects.all()
    context={
        'list':list
    }
    return render(request, 'accounts/hotline.html',context)


def councilorinfro(request):

    infro=councilorinfromation.objects.all()
    context={
        'infro':infro
    }
    return render(request, 'accounts/councilorinfro.html',context)


def search(request):
    givenname = request.POST.get("NIDNumber")
    student = FileAdmin.objects.all().filter(NIDNumber=givenname)
    return render(request, 'accounts/permiisionletter.html', {'file': student})


def others(request):
    # other = Others.objects.all()
    # print(5)
    field_name = 'photo_mayor'
    obj = Others.objects.first()
    field_value = getattr(obj, field_name)
    # print(5)

    return render(request, 'partials/slider.html', {'other': field_value})

def famousplace(request):
    place_list = FamousPlace.objects.all()
    context = {
        'place_list': place_list
    }
    return render(request,'accounts/famousplace.html',context)


class PublicListView(ListView):
    model = uploadbudget
    template_name = 'accounts/uploadbudget.html'


def public_render_pdf_view(request,*args,**kwargs):
    pk=kwargs.get('pk')
    public=get_object_or_404(uploadbudget,pk=pk)

    template_path = 'accounts/pdf2.html'

    context = {'public': public}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



def licencepermissionletter(request):
    context = {'list': FileAdmin.objects.all()}
    return render(request, 'accounts/licencepermiisionletter.html',context)


def download1(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response

    raise Http404
def onlinebd(request):
    context = {'list':OnlineBd.objects.all()}
    return  render(request,'accounts/onlinebdpermissionform.html',context)

def onlinebddwnload(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(fh.read(), content_type="application/document")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
def search1(request):
    PersonalNumber = request.POST.get("PersonalNumber")
    pb1 = OnlineBd.objects.all().filter(PersonalNumber=PersonalNumber)
    return render(request, 'accounts/onlinebdpermissionform.html',{'list': pb1})


def search2(request):
    givenname = request.POST.get("NIDNumber")
    student = FileAdmin.objects.all().filter(NIDNumber=givenname)
    return render(request, 'accounts/licencepermiisionletter.html', {'list': student})