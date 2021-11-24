from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import Group
# Create your views here.


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name="Solicitante")
            user.groups.add(group)
            return redirect("/login")
        else:
            return render(response, "register/register.html", {"form": form})
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})
