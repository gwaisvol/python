from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from users.models import UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import UserProfileForm

def login_user(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request, 'login/login.html', context=context)
    
    elif request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)              
                return render(request, 'welcome.html', context={})

        form = AuthenticationForm()
        context ={
            'form':form,
            'errors':'Usuario o contraseña incorrectos!'
        }
        return render(request, 'login/login.html', context=context)

def register(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context ={
            'form':form
        }
        return render(request, 'register/register.html', context=context)

    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            UserProfile.objects.create(user = user)
            return redirect('/user/login')
        
        context = {
            'errors':form.errors,
            'form':UserCreationForm()
        }
        return render(request, 'register/register.html', context=context)
    
@login_required
def update_user_profile(request):
    user = request.user
    if request.method == 'GET':
        formUpdateProfile = UserProfileForm(initial={
            'phone':request.user.profile.phone,
            'date_of_birth':request.user.profile.date_of_birth,
            'gender': request.user.profile.gender,
            'avatar':request.user.profile.avatar,
        })
        context ={
            'formUpdateProfile':formUpdateProfile
        }
        
        return render(request, 'forms.html', context=context)
    elif request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        for field in form:
            print("Field Error:", field.name,  field.errors)
        if form.is_valid():
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.date_of_birth = form.cleaned_data.get('date_of_birth')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.avatar = form.cleaned_data.get('avatar')
            user.profile.save()
            return redirect('/Products/list-products/')
        
        context = {
            'errors':form.errors,
            'form':UserProfileForm()
        }
        return render(request, 'welcome.html', context=context)  