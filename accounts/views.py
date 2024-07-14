# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm  # Correct import path
from events.models import Event, Publication, Formation


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('/myadmin/')  # Redirect staff users to the admin interface
                else:
                    return redirect('event_list')
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})

def home_view(request):
    events = Event.objects.all()[:5]  # Display the 5 most recent events
    publications = Publication.objects.all()[:5]  # Display the 5 most recent publications
    formations = Formation.objects.all()[:5]  # Adjust the number to display as needed
    return render(request, 'home.html', {'events': events, 'publications': publications, 'formations': formations,})

def logout_view(request):
    logout(request)
    return redirect("login")


