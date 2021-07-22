
from django.shortcuts import render
from account.models import AccountBase as user
from .models import Message

def index(request):
    users = user.objects.all
    return render(request, 'chat/index.html', {'users':users})

def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:25]
    users = user.objects.all
    

    return render(request, 'chat/room.html', {'room_name': room_name, 'username': username, 'messages': messages, 'users': users})