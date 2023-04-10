from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.hashers import make_password, check_password

hashed_pwd = make_password("plain_text")
check_password("plain_text",hashed_pwd)
from .forms import RegistrationForm, ContactForm
# Create your views here.
class Home(View):

    def get(self, request):
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
        print("Hello")
        print(RegistrationForm)
        print("***********")
        return render(request, "register.html", {"user_form": form})

    def post(self, request, *args, **kwargs):
        """
        Function to save new seller data
        """
        form = RegistrationForm(data=self.request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            print("form is valid")   
            password = form.cleaned_data['password']
            # user.set_password(password)
            hashed_pwd = make_password(password)
            check_password("plain_text",hashed_pwd)
            print(hashed_pwd)
            user.password = hashed_pwd
            user.save()
            # message = messages.info(request, "Account created successfully")
        else:
            print("form is not valid") 
            # user_form = forms.RegisterForm()     
            # address_form = forms.AddressForm()
            # message = messages.info(request, "Form is not Valid")
        return render(request, "home.html")


# def login_view(request):
#     if request.method == 'POST':
#         print("********************")
#         username = request.POST.get('email')
#         password = request.POST.get('password')
#         print(username, password)
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             print("user is not None")
#             login(request, user)
#             print("logingggg")
#             return HttpResponseRedirect("/")

#         else:
#             print("User is none")
#             # Add an error message to the context
#             context = {'error': 'Invalid login credentials'}
#     else:
#         context = {}
#         print("E;lse ")
#     return render(request, "login.html")

def login_view(request):
    """
    Login using username and password
    """
    username = password = ""
    if request.POST:
        print("inside the first if")
        username = request.POST["username"]
        password = request.POST["password"]
        
        user_name = request.POST.get("username")
        # if is_seller(user_name) == True or user_name == super_user: 
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            print("inside the second if")

            if user.is_active:
                print("inside the third if")
                login(request, user)
                return HttpResponseRedirect("/")
        else:
                print("elseeeeeeeeeeeeeeeee")
                message = messages.info(request, "You are not registered as seller")
    return render(request, "login.html")
