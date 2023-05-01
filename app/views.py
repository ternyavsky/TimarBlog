from django.shortcuts import render
from users.models import User
from .models import *

def index(request):
    states = State.objects.all()
    comments = Comment.objects.all()
    likes = Like.objects.all()
    context = {
        'states': states,
        'comments':comments,
        'likes':likes
        
        
        }
    return render(request,'index.html', context )


# Create your views here.
