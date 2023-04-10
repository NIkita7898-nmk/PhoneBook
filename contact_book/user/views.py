from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.hashers import make_password, check_password
from .models import User

from .forms import RegistrationForm, ContactForm
# Create your views here.
class Home(View):

    def get(self, request):
        user = User.objects.all()
        return render(request,'home.html')
    
class Register(View):
    
    template_name = "register.html"
    success_url = reverse_lazy("register/")
    # form_class = RegistrationForm
    success_message = "Your profile was created successfully"

    def get(self, request, *args, **kwargs):
        """
        Function to take data from form to register new seller
        """
        form = RegistrationForm
        return render(request, "register.html", {"user_form": form})

    def post(self, request, *args, **kwargs):
        """
        Function to save new seller data
        """
        form = RegistrationForm(data=self.request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            # user.set_password(password)
            hashed_pwd = make_password(password)
            check_password("plain_text",hashed_pwd)
            user.password = hashed_pwd
            user.save()
            message = messages.info(request, "Account created successfully")
            return render(request, "login.html")
        else:
            message = messages.info(request, "Form is not Valid")
            return render(request, "register.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            message = messages.info(request, "Logged in successfully")
            return HttpResponseRedirect("/")
          
        else:
            # Add an error message to the context
            context = {'error': 'Invalid login credentials'}
    else:
        context = {}
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('login') 

class Profile(View):
    def get(self, request):
        user = User.objects.get(email = request.user)
        context = {"user" : user}
        return render(request, 'profile.html', context)