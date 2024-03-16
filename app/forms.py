from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

# Create your forms here.
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 100)
	last_name = forms.CharField(max_length = 100)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)
 

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'level', 'language']
        
class EtabsForm(forms.ModelForm):
    class Meta:
        model = Establishment
        fields = ['manager', 'logo', 'name', 'address', 'mobile', 'email', 'subject', 'module']


class ManagerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

        
class ManagerForm(forms.ModelForm):
    class Meta:
        model= Manager
        fields=['mobile', 'profile_pic']

#for teacher related form
class TeacherUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'password']
        
class TeacherForm(forms.ModelForm):
    class Meta:
        model= Teacher
        fields=['mobile', 'NNI', 'profile_pic', 'diplome', 'subject', 'module', 'langue']