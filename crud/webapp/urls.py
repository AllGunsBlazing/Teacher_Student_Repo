from django.urls import path

from . import views

urlpatterns = [
    
    path('',views.home, name=""),           # when creating an url keep , at the end 

    path('register', views.register, name="register"),
    

    
    
]
