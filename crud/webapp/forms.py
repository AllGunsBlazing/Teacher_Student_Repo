from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms import PasswordInput, TextInput


# - Register/Create a user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        
        # we have two passwords because password1 when the user wants the password and password2 is for confirming the password 

# - Login a user 

class LoginForms(AuthenticationForm) :
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
    # Create a record 
    
class CreateRecordForm(forms.ModelForm):
     class Meta:
            model = Record
            fields = ['first_name','last_name','email','phone','address','city','cgpa','achievement','Internship','Placement','HigherStudies','Entreprenuership','ExtraCurricular','Publications','PractiseSchool','Conference']



 # Update a record 
    
class UpdateRecordForm(forms.ModelForm):
     class Meta:
            model = Record
            fields = ['first_name','last_name','email','phone','address','city','cgpa','achievement','Internship','Placement','HigherStudies','Entreprenuership','ExtraCurricular','Publications','PractiseSchool','Conference']
            

   
















