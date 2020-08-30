from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def createRoomView(request):
    return render(request, 'createRoom.html')


def joinRoomView(request):
    return render(request, 'joinRoom.html')
