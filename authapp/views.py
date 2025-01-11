from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from authapp.models import Conatct

# Create your views here.
def Home(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get("usernumber")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        
        if not username.isdigit() or len(username) != 10:
            messages.info(request, "Phone Number must be 10 Digits")
            return redirect("/signup")

        if pass1 != pass2:
            messages.info(request, "Password does not match")
            return redirect("/signup")

        if User.objects.filter(username=username).exists():
            messages.warning(request, "Phone Number already exists")
            return redirect("/signup")

        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email already exists")
            return redirect("/signup")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, "User is created please login")
        return redirect("/login")
    return render(request, "signup.html")


def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get("usernumber")
        pass1 = request.POST.get("pass1")
        myuser = authenticate(request, username = username, password = pass1)
        if myuser is not None: 
            login(request, myuser)
            # messages.success(request, "You have successfully logged in!")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials. Please try again.")
            return redirect("/login")
    return render(request, "handlelogin.html")

def handlelogout(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect("/login")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("fullname")
        email = request.POST.get("email")
        number = request.POST.get("num")
        desc = request.POST.get("desc")
        myquery = Conatct(name=name, email=email, phonenumber=number, description=desc)
        myquery.save()
        messages.info(request, "Thanks for contacting us. We will get back to you soon")
        return redirect("/contact")
    return render(request, "contact.html")