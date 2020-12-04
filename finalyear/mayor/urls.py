from django.urls import path
from .import views
urlpatterns = [
    path('',views.mayorindex,name="mayorindex"),
    path('officersms/',views.officersms,name="officersms"),
    path('homeviewapplication/',views.homeviewapplication,name="homeviewapplication"),
    path('delete/<id>/', views.delete, name='delete'),
    path('delete1/<id>/', views.delete1, name='delete1'),
    path('ovijok/',views.ovijok,name="ovijok"),
    path('deleteovijok/<id>', views.deleteovijok, name='deleteovijok'),
]