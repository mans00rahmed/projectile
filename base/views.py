from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden

# Create your views here.

rooms = [

        {'id' : 1, 'name': 'Lets learn Python'},
        {'id' : 2, 'name': 'Lets learn Php'},
        {'id' : 3, 'name': 'Lets learn html'},
        {'id' : 4, 'name': 'Lets learn css'},
        {'id' : 5, 'name': 'Lets learn js'},
        {'id' : 6, 'name': 'Lets learn ruby'},
        {'id' : 7, 'name': 'Lets learn R'},
        {'id' : 8, 'name': 'Lets learn c'},
        {'id' : 9, 'name': 'Lets learn c#'},
        
]


# Functions for rendering


def home(request):
    return render(request, 'home.html', {'rooms': rooms})


def room(request,pk):
    for i in rooms:
        if i['id'] == int(pk):
            room=i
    context={'room': room}
    return render(request, 'room.html',context)