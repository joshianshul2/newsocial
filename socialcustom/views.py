# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from django.db.models.functions import Lower
# from django.contrib.auth.models import User,auth
# from .models import User
# from django import forms
# # from .forms import UserLogin
# from django.contrib.auth import authenticate, login
# from django.db.models.functions import Lower
# from django.contrib import  messages
#
# # from django.contrib.auth import (
# #     authenticate,
# #     get_user_model,
# #     login,
# #     logout
# # )
#
# from .forms import UserLoginForm, UserRegisterForm
#
# # Create your views here.
# def signup(request):
#     if request.method == 'POST' :
#         user1=request.POST['Username']
#         # name1=request.POST['name']
#         email1 = request.POST['email']
#         password1 = request.POST['password']
#         # password22 = request.POST['password2']
#         # if password1 == password22 :
#         anji=User(Username=user1,email=email1,password=password1)
#         anji.save()
#         return redirect(index)
#
#     return render(request,'aj.html')
#
#
# def index(request):
#     return render(request,"index.html")
#
# def enter(request):
#     return render(request,"login.html")
#
# def login(request):
#
#     if request.method == 'POST':
#         username= request.POST['username']
#         password= request.POST['password']
#         print(Username)
#         print(password)
#         print(User.object.all())
#         x = auth.authenticate(Username=username, password=password)
#         print("hiii")
#         print(Username)
#         print(password)
#         print(x)
#         return redirect(login)
#         print(x)
#         # if x is  None :
#         #     auth.login(request,x)
#         #     # # return redirect(index)
#         #     return redirect(index)
#         # else:
#         #     messages.info(request,'invalid Credentilas')
#         #     return redirect(index)
#             # print("Anji")
#             # return redirect("https://www.google.com/?client=safari&channel=mac_bm")
#
#     # #
#     else :
#         return render(request,'login.html')
#
#
# # def login_view(request):
# #     next = request.GET.get('next')
# #     form = UserLoginForm(request.POST or None)
# #     if form.is_valid():
# #         username = form.cleaned_data.get('username')
# #         password = form.cleaned_data.get('password')
# #         user = authenticate(username=username, password=password)
# #         login(request, user)
# #         if next:
# #             return redirect(next)
# #         return redirect('/')
# #
# #     context = {
# #         'form': form,
# #     }
# #     return render(request, "login.html", context)
# #
# #
# #
# # def logout_view(request):
# #     logout(request)
# #     return redirect('/')
#
#
#
# def dsa(request) :
#
#     # data = User.objects.all()
#      # data = Students.objects.all()
#     print(objects.Username)
#     data1 = User.objects.order_by(Lower('Username'))
#     # MyModel.objects.order_by(Lower('myfield'))
#     print(User.objects.all())
#     stu = {
#          "dsa1": data1
#          }
#
#     return render(request,"login.html", stu)





from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User,UserManager,Profile1,Profile2

def index(request):
    return render(request, 'index2.html')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    # hashed_password = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
    # password= User.objects.create()
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=request.POST['password'], email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    return redirect('/success')

def login(request):
    if User.objects.filter(email=request.POST['login_email']).exists():
        user = User.objects.filter(email=request.POST['login_email'])[0]
        # if (bcrypt.checkpw(request.POST['login_password'].encode('utf-8'), user.password.encode('utf-8'))):
        if (request.POST['login_password'] == user.password):
            request.session['id'] = user.id
            return redirect('/success')
    return redirect('/')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'index.html', context)

def set_password(self, pw):
    pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    self.password_hash = pwhash.decode('utf8') # decode the hash to prevent is encoded twice

# Fb
def fb(request):
    return render(request,"fb.html")
# twitter
def twitter(request):
    return render(request,"twitter.html")
# linkdien
def linkdien(request):
    return render(request,"linkdien.html")
# insta
def insta(request):
    return render(request,"insta.html")

# profile
def profile(request):
    return render(request,"profile.html")
# About us
def aboutus(request):
    return render(request,"about us.html")

# Save Profile Username and Biography
def saveprofile1(request):
    if request.method == 'POST' :
        user1=request.POST['Username']
        print(user1)
        biography1=request.POST['Biography']
        # name1=request.POST['first_name']
        # name2=request.POST['last_name']
        # email1 = request.POST['email']
        # add1= request.POST['address']
        # add2 = request.POST['address2']
        # city = request.POST['city']
        # # state = request.POST['state']
        # zip = request.POST['zip']
        # anji=Profile(Username=user1,Biography=biography1,first_name=name1,last_name=name2,email=email1,address=add1,address2=add2,city=city,state=state,zip=zip)
        anji=Profile1(Username=user1,Biography=biography1)
        anji.save()
        return redirect(success)

    return render(request,'profile.html')
# Save Profile remaining All
def saveprofile2(request):

    if request.method == 'POST' :
        # user1=request.POST['Username']
        # biography1=request.POST['Biography']
        name1 = request.POST['first_name']
        name2 = request.POST['last_name']
        email1 = request.POST['email']
        add1 = request.POST['address']
        add2 = request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zip']
        anji=Profile2(first_name=name1,last_name=name2,email=email1,address=add1,address2=add2,city=city,state=state,zip=zip)
        anji.save()
        return redirect(success)

    return render(request,'profile.html')

def about_me(request):
    # info = Profile1.objects.all()
    # if request.method == 'POST':
    # user1 = request.POST.get('Username', False)
    # print(user1)
    # if 'Username' in request.POST:
    #     user1 = request.POST['Username']
    # else:
    #     is_private = False
    place = Profile1.objects.get(Username='Anji')
    print(place)
    print(place.id)

    return render(request, "about_me.html",{'info' : place})

# FacebookAPI
def fbapi(request):
    return render(request,"fbapi.html")

