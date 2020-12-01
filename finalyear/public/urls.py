
from django.urls import path
from .import views
urlpatterns = [

    path('',views.publicindex,name="publicindex"),
    path('addproblem/', views.addproblem, name="addproblem"),
    path('applyapplication/', views.applyapplication, name="applyapplication"),
    path('applylicence/', views.applylicence, name="applylicence"),
    path('viewapplylicence/', views.viewapplylicenece, name="viewapplylicence"),
    path('onlinebirthcertificate/', views.onlinebirthcertificate, name="onlinebirthcertificate"),
    path('GivenHomeTax/', views.GivenHomeTax, name="GivenHomeTax"),
    path('sentfeedback/', views.sentfeedback, name="sentfeedback"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<id>/', views.delete, name='delete'),
    path('deshbord/',views.deshbord,name="deshbord"),
    path('logout/',views.logout,name="logout"),


]