from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.hashers import make_password
from .forms import * 
from .models import * 
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime, timedelta, date
from .models import Teacher, Establishment
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import VotreModeleEmail
from django.shortcuts import render
# Create your views here.
def home(request):
    teachers = Teacher.objects.all()
    etab = Establishment.objects.all()
    context = {'teachers': teachers, 'etab':etab}
    return render(request, 'home.html', context)

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, '', ['']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("/")
	form = ContactForm()
	return render(request, "contact.html", {'form':form})

@login_required
def subjects(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'subjects.html', context)


def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subjects')  
    else:
        form = SubjectForm()
    return render(request, 'add_subject.html', {'form': form})

def add_etablissment(request):
    if request.method == 'POST':
        form = EtabsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etabs')  
    else:
        form = EtabsForm()
    return render(request, 'add_etab.html', {'form': form})

def teachers(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'teachers.html', context)

def add_teacher(request):
    if request.method == 'POST':
        user_form = TeacherUserForm(request.POST)
        teacher_form = TeacherForm(request.POST, request.FILES)
        if user_form.is_valid() and teacher_form.is_valid():
            user = user_form.save(commit=False)
            user.password = make_password(user_form.cleaned_data['password']) 
            user.save()
            teacher = teacher_form.save(commit=False)
            teacher.user = user
            teacher.save()
            return redirect('teachers') 
    else:
        user_form = TeacherUserForm()
        teacher_form = TeacherForm()
    return render(request, 'add_teacher.html', {'user_form': user_form, 'teacher_form': teacher_form})

def managers(request):
    managers = Manager.objects.all()
    context = {'managers': managers}
    return render(request, 'managers.html', context)

def add_manager(request):
    if request.method == 'POST':
        user_form = ManagerUserForm(request.POST)
        manager_form = ManagerForm(request.POST, request.FILES)
        if user_form.is_valid() and manager_form.is_valid():
            user = user_form.save(commit=False)
            user.password = make_password(user_form.cleaned_data['password']) 
            user.save()
            manager = manager_form.save(commit=False)
            manager.user = user
            manager.save()
            return redirect('managers') 
    else:
        user_form = ManagerUserForm()
        manager_form = ManagerForm()
    return render(request, 'add_manager.html', {'user_form': user_form, 'manager_form': manager_form})

def etablissement(request):
    etabs = Establishment.objects.all()
    context = {'etabs': etabs}
    return render(request, 'etabs.html', context)




def message(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        your_email = request.POST.get('your_email')
        destination_email = request.POST.get('destination_email')
        message_body = request.POST.get('message_body')

        # Valider les données si nécessaire

        # Envoyer l'e-mail
        try:
            
            send_mail(
                'Sujet du message',
                message_body,
                your_email,
                [destination_email],
                fail_silently=False,
            )
            return HttpResponse('Votre message a été envoyé avec succès !')
        except Exception as e:
            return HttpResponse('Une erreur s\'est produite lors de l\'envoi du message : ' + str(e))

    else:
        emails = VotreModeleEmail.objects.all()
        return render(request, 'message.html', {'emails': emails})



def services(request):
    teachers = Teacher.objects.all()
    establishments = Establishment.objects.all()
    context = {
        'teachers': teachers,
        'establishments': establishments,
    }
    return render(request, 'base.html', context)