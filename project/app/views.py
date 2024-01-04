from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required 
def dashboard(request):
    username = request.user.username
    welcome_message = f"Welcome, {username}!"
    context = {'welcome_message': welcome_message}
    return render(request, 'dashboard.html', context)

def logout(request):
    auth.logout(request)
    print('User Logged Out!!')
    return redirect('login')

@login_required
def profile(request):
    context = {}
    username = request.user.username
    email =  request.user.email
    context['username'] = username
    context['email'] = email
    
    return render(request,'profile.html',context)
def register(request):  
    if request.method == "POST":
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        username = request.POST.get('username').lower()
        if password1 == password2:
            # Check if the username or email is already in use
            if User.objects.filter(username=username).exists(): 
                print('username exists')       
                return render(request, 'register.html', {'error': 'Username is already in use.'})
            
            elif User.objects.filter(email=email).exists(): 
                print('username exists')       
                return render(request, 'register.html', {'error': 'Email is already in use.'})

            # Create and save the user
            user = User.objects.create_user(username=username, email=email, password=password1)
            print('user created')
            return redirect('login')
        else:
            # If Passwords do not match
            return render(request, 'register.html', {'error': 'Passwords do not match.'})  
    return render(request, 'register.html'  )  
        
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        # Check if the username_or_email is an email
        if '@' in email:
            print('@')
            try:
                obj = User.objects.get(email=email)
                print(obj)
                user = authenticate(request, username= obj.username, password=password)
                print('1')
            except:
                return render(request, 'login.html', {'error': 'Invalid email or password.'})
        else:
            try:
                user = authenticate(request, username=email, password=password)
                print('2')
            except:
                pass
        
        print('username is correct')
        if user is not None:
            print('user logged in')
            auth.login(request, user)
            return redirect('dashboard')
        else:
            #Invalid username or password
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')