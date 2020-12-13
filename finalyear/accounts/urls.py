"""finalyear URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .import views
from django.views.static import serve
from django.conf import settings
from .views import PublicListView,public_render_pdf_view ,onlinebd
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name="index"),
    path('registration', views.registration, name="registration"),
    path('login', views.login, name='login'),
    path('solveproblem/',views.solveproblem,name="solveproblem"),
    path('permissionletter/',views.permissionletter,name="permissionletter"),
    path('schoolcollege/',views.schoolcollege,name="schoolcollege"),
    path('officernotice/',views.officernotice,name="officernotice"),
    path('number/',views.number,name="number"),
    url(r'^download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('councilorinfro/',views.councilorinfro,name='councilorinfro'),
    path('search', views.search, name="search"),
    path('other/',views.others,name="other"),
    path('place/',views.famousplace,name="place"),
    path('PublicListView/',PublicListView.as_view(),name='PublicListView'),
    path('pdf/<pk>/',public_render_pdf_view,name="public_render_pdf_view"),
    path('licencepermissionletter/',views.licencepermissionletter,name='licencepermissionletter'),
    url(r'^download1/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('onlinebd/',views.onlinebd,name="onlinebd"),
    url(r'^onlinebddwnload/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('search1', views.search1, name="search1"),
    path('search2', views.search2, name="search2"),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_complete"),




]
