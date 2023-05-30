from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return redirect('/dashboard/')

def dashboard(request):
    return HttpResponse("dashboard")
