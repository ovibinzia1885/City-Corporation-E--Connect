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


]