from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password

def register(request):
    """
    This function handles the registration of a new user. 
    If the request method is 'POST', it creates a new form instance using the 
    UserCreationForm class and the data from the request. If the form is valid, 
    it hashes the password, creates a new user object, sets the hashed password as 
    the user's password, saves the user, logs the user in, and redirects them to 
    the home page. If the request method is not 'POST', it creates a new empty 
    form instance and renders the 'users/register.html' template with the form as 
    a context variable.
    """

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            hashed_password = make_password(form.cleaned_data.get('password1'))
            user = form.save(commit=False)
            user.password = hashed_password
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})



def login_view(request):
    """Handles user login.
    
    Checks if the request method is 'POST'. If so, it retrieves the
    username and password from the request, calls Django's authenticate()
    function to verify the user's identity, and logs in the user if
    the credentials are valid. If the credentials are not valid, an
    error message is displayed and the user is redirected back to the
    login page. If the request method is not 'POST', the login page
    is rendered.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'Invalid login credentials')
            return render(request, 'users/login.html')
    return render(request, 'users/login.html')


def loggedIn(request): 
    return render(request, 'home')

def logout_view(request):
    logout(request)
    return redirect('home')


def home(request):
    return render(request, 'users/home.html')
