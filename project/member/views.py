# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from project.member.forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
import pymysql
# Create your views here.

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/../')
        else:
            return HttpResponse('loginerror')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid() and request.POST['password']==request.POST['passwordConfirm']:
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('/')
        else :
            return HttpResponse('registerError')