from django.shortcuts import render, HttpResponse,redirect
from . forms import RegistrationsForm ,LoginForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate ,logout
def signup(request):
    form = RegistrationsForm()
    if request.method == 'POST':
        form = RegistrationsForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        return render(request,'signup.html',{'form':form})
    return render(request,'signup.html',{'form':form})


def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html',{"form":form})
        # return render(request,'login.html',{'form':form})
    return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('/')