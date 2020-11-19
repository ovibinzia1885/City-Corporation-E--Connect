from django.urls import path
from .import views
urlpatterns = [
    path('',views.mayorindex,name="mayorindex"),
    path('homeviewapplication/',views.homeviewapplication,name="homeviewapplication"),
    path('delete/<id>/', views.delete, name='delete'),
]