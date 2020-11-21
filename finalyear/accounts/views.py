import os

from django.conf import settings
from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.urls import reverse
from django.contrib.auth.models import User
from mayor.models import FileAdmin
from .models import Others



from django.http import HttpResponseRedirect, Http404, HttpResponse

# Create your views here.
from userprofile.models import UserRole


def index(request):
    return render(request,'accounts/index.html')

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
                    UserRole.objects.create(user=user, role=usertype,)
                    messages.success(request, 'You are successfully registered!')
                    return HttpResponseRedirect(reverse('login'))
        else:
            messages.error(request, 'Password does not match!')

        return HttpResponseRedirect(reverse('registration'))

    #	return redirect('user-register') # not standard


    return render(request,'accounts/registration.html')
def login(request):

    if request.method == "POST":
        method_dict = request.POST.copy()
        username = method_dict.get('username')
        password = method_dict.get('password')

        user = auth.authenticate(username=username, password=password,)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are successfully logged in!')
            # return HttpResponseRedirect(reverse('index'))
            if request.user.userrole.role == 'mayor':
                return render(request,'mayor/mayorindex.html')
            elif request.user.userrole.role == 'officer':
                return render(request,'officer/officerindex.html')
            elif request.user.userrole.role == 'public':
                return render(request,'public/publicindex.html')
        else:
            messages.error(request, 'Invalid Credentials!')
            return HttpResponseRedirect(reverse('login'))

    return render(request,'accounts/login.html')

def solveproblem(request):
    return render(request,'accounts/solveproblem.html')
def permissionletter(request):
    context = {'file': FileAdmin.objects.all()}
    return render(request,'accounts/permiisionletter.html',context)

def download(request,path):
	file_path=os.path.join(settings.MEDIA_ROOT,path)
	if os.path.exists(file_path):
		with open(file_path,'rb')as fh:
			response=HttpResponse(fh.read(),content_type="application/adminupload")
			response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
			return response

	raise Http404

def schoolcollege(request):
    return render(request,'accounts/schoolcollege.html')
def notice(request):
    return render(request,'accounts/notice.html')
def hotline(request):
    return render(request,'accounts/hotline.html')
def councilorinfro(request):
    return render(request,'accounts/councilorinfro.html')

