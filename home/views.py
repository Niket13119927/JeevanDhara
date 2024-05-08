from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from home.forms import Patientform

def home(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def signup_p(request):
    form=Patientform()
    if request.method == 'POST':
        form=Patientform(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        blood_group = request.POST.get('blood_group')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = name
        # Set additional fields if necessary
        user.save()
        form.save()
    

        # Log the user in
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'There was a problem with your signup data. Please try again.')
            return redirect('signup_p')
    data={
        'form': form
    }
    return render(request, 'signup_p.html',data)

def signup_h(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        # Add any other form fields here

        # Create the user
        user = User.objects.create_user(username=username, password=password, email=email)
        # Save the user object
        user.save()
        

        # Log the user in
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'There was a problem with your signup data. Please try again.')
            return redirect('signup_h')
    else:
        return render(request, 'hlogin.html')

def signin_p(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect.')
            return redirect('signin_p')
    else:
        return render(request, 'plogin.html')

def signin_h(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect.')
            return redirect('signin_h')
    else:
        return render(request, 'hlogin.html')

def signout(request):
    logout(request)

    return redirect('home')

def bloodtype(request):
    return render(request,'bloodtype.html')
def hospital(request):
    return render(request,'hospital.html')
def ambulance(request):
    return render(request,'ambulance.html')
def about(request):
    return render(request,'about.html')

