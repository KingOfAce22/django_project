from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.models import User 

# Create your views here.
def index(request):
    return render(request,'base.html')

def signup(request):
    if request.method=="POST":
        # Get the post parameters
        name=request.POST['name']
        email=request.POST['email']
        dob=request.POST['dob']
        phone=request.POST['phone']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('signup')

        myuser = User.objects.create_user(name, email, pass1)
        myuser.date_of_birth= dob
        myuser.phoneno= phone
        myuser.save()
        messages.success(request, " Your ID has been successfully created . Please Login !!!")
        return redirect('index')

    else:
        return render(request,"signup.html")

    

def handlelogin(request):
    if request.method=="POST":
        loginname = request.POST['name']
        loginpassword = request.POST['loginpassword']
        user = authenticate(request,username=loginname,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"You have logged in successfully")
            return redirect('index')
        else:
            messages.error(request,"Invalid credential ! Please try again...")
    else:
        return render(request,'login.html')


def handlelogout(request):
        logout(request)
        messages.success(request,"You have successfully logout...")
        return redirect('index')