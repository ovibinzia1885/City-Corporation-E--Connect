
from django.urls import path
from .import views
urlpatterns = [
    path('public/',views.publicindex,name="publicindex"),
    path('addproblem',views.addprobelm,name="addproblem"),

]