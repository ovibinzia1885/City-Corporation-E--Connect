
from django.urls import path
from .import views
urlpatterns = [

    path('',views.publicindex,name="publicindex"),
    path('addproblem/', views.addproblem, name="addproblem"),
    path('applyapplication/', views.applyapplication, name="applyapplication"),
    path('applylicence/', views.applylicence, name="applylicence"),
    path('onlinebirthcertificate/', views.onlinebirthcertificate, name="onlinebirthcertificate"),
    path('GivenHomeTax/', views.GivenHomeTax, name="GivenHomeTax"),
    path('FeedBack/', views.FeedBack, name="FeedBack"),


]