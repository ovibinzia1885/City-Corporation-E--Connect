from django.urls import path
from .import views
urlpatterns = [
    path('officer/',views.officerindex,name="officrindex")

]