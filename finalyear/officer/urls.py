from django.urls import path
from .import views
urlpatterns = [
    path('',views.officerindex,name="officer"),
    path('Feedback/',views.Feedback,name="Feedback"),
    path('taxview/', views.taxview, name="taxview"),
    path('Smsmayor/', views.Smsmayor, name="Smsmayor"),
    path('viewcertificate/', views.viewcertificate, name="viewcertificate"),
    path('licenceview/', views.licenceview, name="licenceview"),
    path('viewproblem/', views.viewproblem, name="viewproblem"),
    path('workshop/', views.workshop, name="workshop"),
    path('officerviewapplylicenece/', views.officerviewapplylicenece, name="officerviewapplylicenece"),
    path('delete/<id>/', views.delete, name='delete'),
    path('delete1/<id>/', views.delete1, name='delete1'),
    path('delete2/<id>/', views.delete2, name='delete2'),
    path('wardno1/',views.wardno1,name="wardno1"),
    path('wardno/2',views.wardno2,name="wardno2"),
    path('wardno3/',views.wardno3,name="wardno3"),



]