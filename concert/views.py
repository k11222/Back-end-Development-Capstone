from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.hashers import make_password

from concert.forms import LoginForm, SignUpForm
from concert.models import Concert, ConcertAttending
import requests as req


# Create your views here.

def signup(request):
    pass


def index(request):
    return render(request, "index.html")


   def songs(request):
    songs = {"songs":[{"id":1,"title":"duis faucibus accumsan odio curabitur convallis","lyrics":"Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis."}]}
    return render(request, "songs.html", {"songs":songs["songs"]})

def photos(request):
    photos = [{
    "id": 1,
    "pic_url": "http://dummyimage.com/136x100.png/5fa2dd/ffffff",
    "event_country": "United States",
    "event_state": "District of Columbia",
    "event_city": "Washington",
    "event_date": "11/16/2022"
    }]
    return render(request, "photos.html", {"photos": photos})

def login_view(request):
    pass

def logout_view(request):
    pass

def concerts(request):
    pass


def concert_detail(request, id):
    if request.user.is_authenticated:
        obj = Concert.objects.get(pk=id)
        try:
            status = obj.attendee.filter(user=request.user).first().attending
        except:
            status = "-"
        return render(request, "concert_detail.html", {"concert_details": obj, "status": status, "attending_choices": ConcertAttending.AttendingChoices.choices})
    else:
        return HttpResponseRedirect(reverse("login"))
    pass


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.filter(username=username).first()
            if user:
                return render(request, "signup.html", {"form": SignUpForm, "message": "user already exist"})
            else:
                user = User.objects.create(
                    username=username, password=make_password(password))
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
        except User.DoesNotExist:
            return render(request, "signup.html", {"form": SignUpForm})
    return render(request, "signup.html", {"form": SignUpForm})
