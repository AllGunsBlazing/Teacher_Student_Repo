from django.urls import path

from . import views

urlpatterns = [
    
    path('',views.home, name=""),           # when creating an url keep , at the end 

    path('register', views.register, name="register"),
    
    path('login', views.login, name="login"),
    
    path('user-logout',views.user_logout,name="user-logout"),
    
    
    # route name should be same as views
    
    # CRUD
    
    path('dashboard', views.dashboard,name="dashboard"),
    path('create-record', views.create_record,name="create-record"),
    




    
    
    
    
]
