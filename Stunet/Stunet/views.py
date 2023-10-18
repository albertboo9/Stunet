#B. Albert

from django.shortcuts import render, redirect
from datetime import datetime
from Stunet.forms import LoginForm, StudentProfileForm, EmployeeProfileForm

def welcome(request):
    return render(request, 'welcome.html',
                  {'current_date_time': datetime.now})


def login(request):
    #teste si le formulaire a été envoyé
    if len(request.POST) > 0:
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('/welcome')
        else:
            return render(request, 'login.html', {'form':form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})


def register(request):
    if len(request.GET) > 0 and ('profileType' in request.GET):
        studentForm = StudentProfileForm(prefix="st")
        employeeForm = EmployeeProfileForm(prefix="em")
        if request.GET['profileType'] == 'student':
            studentForm = StudentProfileForm(request.GET, prefix="st")
            if studentForm.is_valid():
                studentForm.save()
                return redirect('/login')
            elif request.GET['profileType'] == 'employee':
                employeeForm = EmployeeProfileForm(request.GET, prefix="em")
                if employeeForm.is_valid():
                    employeeForm.save()
                    return redirect('/login')
            #Le formulaire n'est pas valide 
            return render(request, 'user_profile.html', 
                                            {'studentForm': studentForm,
                                             'employeeForm': employeeForm})
    else:
        studentForm = StudentProfileForm(prefix="st")
        employeeForm = EmployeeProfileForm(prefix="em")
        return render(request, 'user_profile.html',
                                        {'studentForm': studentForm,
                                        'employeeForm': employeeForm})
        
