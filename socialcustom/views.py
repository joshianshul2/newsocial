from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import render_to_response
from django.db.models.functions import Lower
from .models import User

# Create your views here.
def signup(request):
    if request.method == 'POST' :
        user1=request.POST['Username']
        # name1=request.POST['name']
        email1 = request.POST['email']
        password1 = request.POST['password']
        # password22 = request.POST['password2']
        # if password1 == password22 :
        anji=User(Username=user1,email=email1,password=password1)
        anji.save()

    return render(request,'aj.html')


def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")
