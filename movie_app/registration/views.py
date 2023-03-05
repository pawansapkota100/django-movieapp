from django.contrib.auth.models import User 
# for authentication in login page
from django.contrib.auth import authenticate,login,logout

#for inserting value from signup form to user
from django.shortcuts import render,redirect, HttpResponse

# to not to give access to home page if user hit url of home page directly
from django.contrib.auth.decorators import login_required

# Create your views here.
@ login_required(login_url='login')
def homepage(request):
     return render(request,'index.html')


def signuppage(request):
    if request.method=='POST':
    
        name=request.POST.get('name')
        username=request.POST.get('username')
        password=request.POST.get('password')
# assigning the value of form into user of db
        my_user= User.objects.create_user(name, username,password)
        my_user.save()
        return redirect('login')

        
    
    return render(request,'signup.html')

def loginpage(request):
    if request.method=='POST':
        usern=request.POST.get('username')
        passw=request.POST.get('password')

        # for authentication
        user= authenticate(request, username=usern, password=passw)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
             return HttpResponse("incorrect username or password")
  
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')
