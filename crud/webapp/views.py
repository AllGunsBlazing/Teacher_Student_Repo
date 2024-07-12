from django.shortcuts import render, redirect, get_object_or_404

from .forms import CreateUserForm, LoginForms , CreateRecordForm, UpdateRecordForm

from django.http import JsonResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from .models import Record
from .utils import fetch_google_sheets_data, upload_file_to_drive

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
    sort_by = request.GET.get('sort_by', 'id')  # Default sorting by id
    sort_order = request.GET.get('sort_order', 'asc')  # Default sorting order is ascending
    filter_by = request.GET.get('filter', None)
    
    if sort_order == 'desc':
        sort_by = f'-{sort_by}'
    
    records = Record.objects.all().order_by(sort_by)
    
    if filter_by:
        if filter_by == 'placement':
            records = records.exclude(Placement__isnull=True).exclude(Placement__exact='')
        elif filter_by == 'internship':
            records = records.exclude(Internship__isnull=True).exclude(Internship__exact='')
        elif filter_by == 'achievement':
            records = records.exclude(achievement__isnull=True).exclude(achievement__exact='')
        elif filter_by == 'higher_studies':
            records = records.exclude(HigherStudies__isnull=True).exclude(HigherStudies__exact='')
        elif filter_by == 'entrepreneurship':
            records = records.exclude(Entreprenuership__isnull=True).exclude(Entreprenuership__exact='')
        elif filter_by == 'extra_curricular':
            records = records.exclude(ExtraCurricular__isnull=True).exclude(ExtraCurricular__exact='')
        elif filter_by == 'publications':
            records = records.exclude(Publications__isnull=True).exclude(Publications__exact='')
        elif filter_by == 'practise_school':
            records = records.exclude(PractiseSchool__isnull=True).exclude(PractiseSchool__exact='')
        elif filter_by == 'conference':
            records = records.exclude(Conference__isnull=True).exclude(Conference__exact='')

    
    context = {'records': records, 'sort_by': sort_by.strip('-'), 'sort_order': sort_order}
    return render(request, 'webapp/dashboard.html', context=context)

# - Create a Record 
@login_required(login_url='login')
def create_record(request):
    if request.method == "POST":
        form = CreateRecordForm(request.POST, request.FILES)

        if form.is_valid():
            record = form.save(commit=False)

            # Upload files to Google Drive and set URLs to the corresponding fields
            if 'achievement' in request.FILES:
                record.achievement = upload_file_to_drive(request.FILES['achievement'])
            if 'Internship' in request.FILES:
                record.Internship = upload_file_to_drive(request.FILES['Internship'])
            if 'Placement' in request.FILES:
                record.Placement = upload_file_to_drive(request.FILES['Placement'])
            if 'HigherStudies' in request.FILES:
                record.HigherStudies = upload_file_to_drive(request.FILES['HigherStudies'])
            if 'Entreprenuership' in request.FILES:
                record.Entreprenuership = upload_file_to_drive(request.FILES['Entreprenuership'])
            if 'ExtraCurricular' in request.FILES:
                record.ExtraCurricular = upload_file_to_drive(request.FILES['ExtraCurricular'])
            if 'Publications' in request.FILES:
                record.Publications = upload_file_to_drive(request.FILES['Publications'])
            if 'PractiseSchool' in request.FILES:
                record.PractiseSchool = upload_file_to_drive(request.FILES['PractiseSchool'])
            if 'Conference' in request.FILES:
                record.Conference = upload_file_to_drive(request.FILES['Conference'])

            # Save the record to the database
            record.save()

            return redirect("dashboard")
    
    form = CreateRecordForm()
    context = {'form': form}
    
    return render(request, 'webapp/create-record.html', context=context)

# -  update a record 

@login_required(login_url='my-login')
def update_record(request,pk): 
    
    record = Record.objects.get(id=pk)

# Change this line in your views.py file
    form = UpdateRecordForm(instance=Record)
    
    if request.method == 'POST':
         form = UpdateRecordForm(request.POST,instance=record)
         
         if form.is_valid():
             
             form.save()
             return redirect("dashboard")

    return render(request, 'webapp/update-record.html',context=context)

# - Read / View a singular record  

    @login_required(login_url='my-login')
    def update_record(request, pk):
        
        all_records = Records.object.get(id=pk)
        
        context = {'record':all_records}
        
        return render(request, 'webapp/view-record.html', context=context)
        
    



    













# User Logout 

def user_logout(request): 
    
    auth.logout(request)
    
    return redirect("login")

    
# Upload File

@login_required(login_url='login')
def upload_file(request, record_id, field_name):
    record = get_object_or_404(Record, id=record_id)
    
    if request.method == 'POST' and 'file' in request.FILES:
        uploaded_file = request.FILES['file']
        drive_url = upload_file_to_drive(uploaded_file)
        
        if drive_url:
            if field_name == 'achievement':
                record.achievement = drive_url
            elif field_name == 'Internship':
                record.Internship = drive_url
            elif field_name == 'Placement':
                record.Placement = drive_url
            elif field_name == 'HigherStudies':
                record.HigherStudies = drive_url
            elif field_name == 'Entreprenuership':
                record.Entreprenuership = drive_url
            elif field_name == 'ExtraCurricular':
                record.ExtraCurricular = drive_url
            elif field_name == 'Publications':
                record.Publications = drive_url
            elif field_name == 'PractiseSchool':
                record.PractiseSchool = drive_url
            elif field_name == 'Conference':
                record.Conference = drive_url
            
            record.save()
        return redirect('dashboard')
    
    return redirect('dashboard')    
        

@login_required(login_url='login')
def fetch_sheets_data(request):
    try:
        data = fetch_google_sheets_data()
        return redirect('dashboard')
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
        