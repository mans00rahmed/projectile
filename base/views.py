from multiprocessing import context
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.db.models import Q
from .forms import RoomForm
from .models import Room, Topic

# Create your views here.

# rooms = [

#         {'id' : 1, 'name': 'Lets learn Python'},
#         {'id' : 2, 'name': 'Lets learn Php'},
#         {'id' : 3, 'name': 'Lets learn html'},
#         {'id' : 4, 'name': 'Lets learn css'},
#         {'id' : 5, 'name': 'Lets learn js'},
#         {'id' : 6, 'name': 'Lets learn ruby'},
#         {'id' : 7, 'name': 'Lets learn R'},
#         {'id' : 8, 'name': 'Lets learn c'},
#         {'id' : 9, 'name': 'Lets learn c#'},
#         {'id' : 10, 'name': 'Lets learn C++'},
        
        
# ]


# Functions for rendering

def loginPage(request):
        if request.user.is_authenticated:
                return redirect('home')
        if request.method == 'POST':
                username=request.POST.get('username')
                password=request.POST.get('password')

                try:
                        user=User.objects.get(username=username)
                except:
                        messages.error(request, 'User Not Fount.')

                user = authenticate(request,username=username,password=password)

                if user is not None:
                        login(request,user)
                        return redirect('home')
                else:
                        messages.error(request, 'Username or Password Not Exists.')

        context={}
        return(render(request, 'base/login_register.html', context))

def logoutUser(request):
        logout(request)
        return redirect('home')

def home(request):
        q=request.GET.get("q") if request.GET.get("q") != None else ''
        rooms = Room.objects.filter(
                Q(topic__name__icontains=q) |
                Q(name__icontains=q) |
                Q(description__icontains=q)
                )
        topics = Topic.objects.all()
        room_count=rooms.count()
        return render(request, 'home.html', {'rooms': rooms,'topics':topics, 'room_count':room_count })

def room(request,pk):
    room = Room.objects.get(id=pk)
    context={'room': room}
    return render(request, 'room.html',context)

@login_required(login_url='login')
def create_room(request):
        form = RoomForm()
        if request.method == 'POST':
                form = RoomForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('home')

        context={'form': form}
        return(render(request, 'base/room_form.html', context))

@login_required(login_url='login')
def update_room(request,pk):
        room = Room.objects.get(id=pk)
        form = RoomForm(instance=room)
        if request.user != room.host:
                return HttpResponse("You are not allowed here")
        if request.method == 'POST':
                form = RoomForm(request.POST, instance=room)
                if form.is_valid():
                        form.save()
                        return redirect('home')
        context={'form': form}
        return render(request, 'base/room_form.html',context)
@login_required(login_url='login')

def delete_room(request,pk):
        room = Room.objects.get(id=pk)

        if request.user != room.host:
                return HttpResponse("You are not allowed here")

        if request.method=='POST':
                room.delete()
                return redirect('home')

        return render(request, 'base/delete.html',{'obj':room})

