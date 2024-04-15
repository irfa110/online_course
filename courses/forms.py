from django import forms
from django.contrib.auth import authenticate ,login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth.models import User
from django.forms import ValidationError


class RegistrationsForm(UserCreationForm):
    first_name = forms.CharField(max_length=50,required = True)
    last_name = forms.CharField(max_length=50,required = True)
    email = forms.EmailField(max_length=50,required = True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        user = None
        try:
            user = User.objects.get(email = email)
        except:
            return email

        if user is not None:
            raise ValidationError("Email alredy register")


class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=50,required = True,label="Email Address")

    def clean(self):
        email = self.cleaned_data['username']
        password = self.changed_data['password']
        print(email,password,'$$$$$$$$$$$$')
        user = None
        try:
            user = User.objects.get(email=email)
            result =   authenticate(username = user.username,password = password)
            print(result)
            if (result is not None):
                login(self.request,result)
                return result
            else:
                raise ValidationError("Email or password inviled")
        except:
            raise ValidationError("Email or password inviled")
