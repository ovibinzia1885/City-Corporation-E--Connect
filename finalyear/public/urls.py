
from django.urls import path
from .import views
urlpatterns = [

    path('',views.publicindex,name="publicindex"),
    path('addproblem/', views.addproblem, name="addproblem"),


]