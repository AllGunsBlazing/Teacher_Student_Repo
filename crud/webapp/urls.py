from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

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
    
    path('update-record/<int:pk>', views.update_record,name='update-record'),       #dynamic 

    path('record/<int:pk>', views.update_record, name="record"),
    
    path('upload_file/<int:record_id>/<str:field_name>/', views.upload_file, name='upload_file'),
    
    path('fetch-sheets-data', views.fetch_sheets_data, name='fetch-sheets-data'),
]
