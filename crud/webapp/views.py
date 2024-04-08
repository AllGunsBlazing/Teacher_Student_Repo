from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForms

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from .models import Record


# - Homepage

def home(request):
    

    return render(request, 'webapp/index.html') 

# - Register a user 

def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":    # if we are making a post request from our register.html page which is we are sending data to our database
        
        form = CreateUserForm(request.POST)

        if form.is_valid():
            
            form.save()

            return redirect('login')
           
    context = {'form':form}
    
    return render(request, 'webapp/register.html',context=context)

# - LOGIN A USER

def login(request):
    form = LoginForms()
    
    if request.method == "POST":
        
        form = LoginForms(request, data=request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                
                auth.login(request, user)
            
                return redirect('dashboard')
            
            
    context = {'form': form}

    return render(request, 'webapp/login.html', context=context)


# - Dashboard

@login_required(login_url='login')
def dashboard(request):
    
    
    my_records = Record.objects.all()

    context = {'records': my_records}
    
    return render(request,'webapp/dashboard.html', context=context)














# User Logout 

def user_logout(request): 
    
    auth.logout(request)
    
    return redirect("login")

    



        
        
        
        
        
        