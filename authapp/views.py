from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from authapp.models import Contact, MembershipPlan, Enrollment,Trainer, Gallery, Workout, CustAttendance, GymImage, GymContact, Facility, GymAddress, Services

from django.db import models
# Create your views here.
def Home(request):
    return render(request, "index.html")

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    user_phone=request.user
    posts=Enrollment.objects.filter(PhoneNumber=user_phone)
    attendance=CustAttendance.objects.filter(phonenumber=user_phone)
    
       
    context={"posts":posts,"attendance":attendance}
    return render(request,"profile.html",context)


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
        myquery = Contact(name=name, email=email, phonenumber=number, description=desc)
        myquery.save()
        messages.info(request, "Thanks for contacting us. We will get back to you soon")
        return redirect("/contact")
    return render(request, "contact.html")

def enrollment(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')

    Membership=MembershipPlan.objects.all()
    SelectTrainer=Trainer.objects.all()
    context={"Membership":Membership,"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        FullName=request.POST.get('FullName')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        PhoneNumber=request.POST.get('PhoneNumber')
        DOB=request.POST.get('DOB')
        member=request.POST.get('member')
        trainer=request.POST.get('trainer')
        reference=request.POST.get('reference')
        address=request.POST.get('address')
        query=Enrollment(FullName=FullName,Email=email,Gender=gender,PhoneNumber=PhoneNumber,DOB=DOB,SelectMembershipPlan=member,SelectTrainer=trainer,reference=reference,Address=address)
        query.save()
        messages.success(request,"Thanks For Enrollment")
        return redirect('/join')



    return render(request,"enroll.html",context)

def gallery(request):
    posts=Gallery.objects.all()
    context={"posts":posts}
    return render(request, "gallery.html", context)

def about_us(request):
    gym_images = GymImage.objects.all()
    contacts = GymContact.objects.all()
    facilities = Facility.objects.all()
    gym_address = GymAddress.objects.all()
    return render(request, 'about.html', {
        'gym_images': gym_images,
        'contacts': contacts,
        'facilities': facilities,
        'gym_address': gym_address,
    })


def service(request):
    services = Services.objects.all()
    return render(request, "service.html", {'services': services})

def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login and Try Again")
        return redirect('/login')
    SelectTrainer=Trainer.objects.all()
    SelectWorkout=Workout.objects.all()
    context={"SelectTrainer":SelectTrainer, "SelectWorkout":SelectWorkout}
    if request.method=="POST":
        UserNumber= request.POST.get("PhoneNumber")
        Workouts=request.POST.get("workout")
        LoginTime= request.POST.get("logintime")
        LogoutTime= request.POST.get("logouttime")
        TrainedBy= request.POST.get("trainer")
        Status= request.POST.get("status")
        query= CustAttendance(phonenumber=UserNumber, Workout= Workouts, LoginTime=LoginTime, LogoutTime=LogoutTime, TrainedBy=TrainedBy, Status=Status)
        query.save()
        messages.success(request,"Successfully Applied!")
        return redirect('/attendance')
    return render(request, "attendance.html", context)