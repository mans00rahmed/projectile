from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from .models import Room
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


def home(request):
        rooms = Room.objects.all()
        return render(request, 'home.html', {'rooms': rooms})


def room(request,pk):
    room = Room.objects.get(id=pk)
    context={'room': room}
    return render(request, 'room.html',context)