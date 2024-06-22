from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def register_view(request):

    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('home') 

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})



def login_view(request):

    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('home') 
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, "Successfully Logged In!")

            if request.POST.get('remember'):
                request.session.set_expiry(1209600)
            else:
                request.session.set_expiry(0)
            return redirect('home')
        
        else:
            error_message = "Invalid username or password"
            return render(request, 'accounts/login.html', {'error_message':error_message})

    context= {}
    
    return render(request, 'accounts/login.html', context)


def logout_view(request):

    if request.user.is_authenticated:
        logout(request)

    return redirect('login')
