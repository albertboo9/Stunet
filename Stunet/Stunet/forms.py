
from django import forms
from Stunet.models import Person, Student , Employee

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Mot de passe', 
                               widget=forms.PasswordInput)
    
    def clean(self):
        Cleaned_data = super(LoginForm, self).clean()
        email = Cleaned_data.get("email")
        password = Cleaned_data.get("password")


        #vérifions si les deux champs sont valides
        
        if email and password:
            result = Person.objects.filter(password=password, 
                                           email=email)
            if len(result) != 1:
                raise forms.ValidationError("Adresse mail ou mot de passe érroné(e).")
        return Cleaned_data

    
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('friends', )
    


class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = Employee 
        exclude = ('friends', )
        