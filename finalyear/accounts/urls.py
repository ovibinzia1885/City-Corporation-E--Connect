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
from .views import PublicListView,public_render_pdf_view


urlpatterns = [
    path('',views.index,name="index"),
    path('registration', views.registration, name="registration"),
    path('login', views.login, name='login'),
    path('solveproblem/',views.solveproblem,name="solveproblem"),
    path('permissionletter/',views.permissionletter,name="permissionletter"),
    path('schoolcollege/',views.schoolcollege,name="schoolcollege"),
    path('notice/',views.notice,name="notice"),
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




]
