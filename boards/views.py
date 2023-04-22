from django.shortcuts import render,redirect
from django.http import HttpResponse
from boards.models import Board,recherche,Video
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    video = Video.objects.all()
    boards = recherche.objects.all()
    if (request.method == "POST"):
        recherches = request.POST['recherche']
        input = recherche(input = recherches)
        input.save()
    a=len(video)
    return render(request,'youtube.html',{'boards':boards,'video':video,'nom':a})
def video(request):
    video = Video.objects.all()
    video_id = request.GET.get('id')
    video1 = Video.objects.get(id = video_id)
    dicte = {
        'video':video,
        'video1':video1,
    }
    return render(request,'video.html',dicte)
def qwiz(request):
    video = Video.objects.all()
    video_id = request.GET.get('id')
    video1 = Video.objects.get(id = video_id)
    video2 = video1.questions.all()
    video = Video.objects.all()
    dicte = {
        'video':video,
        'video1':video1,
        'related_questions':video2,
    }
    return render(request,'qwiz.html',dicte)
def register(request):
        if request.method == "POST":
              username = request.POST['username']
              first_name = request.POST["first_name"]
              last_name = request.POST["last_name"]
              Email = request.POST["email"]
              password = request.POST["password"]
              Email = request.POST["email"]
              Confirm_Password = request.POST["Confirm Password"]
              user = User.objects.create_user(username,Email,password)
              user.last_name = last_name
              user.first_name = first_name
              user.save()
              messages.success( request, 'you account was succesfully created')
              message = "your acount was seccevfuly created"
              return render(request,'login.html',{'messages':message})
        else: 
              message = "error "
              return render(request,'register.html',{'messages':message})
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request, user)
          return redirect('home')
        else:
           messages.success(request,("error"))
           return redirect('login')
    else:
          return render(request,"login.html",{})
def logout(request):
        pass
def index(request):
      return(render(request,'index.html'))