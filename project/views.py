# -*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.

def main(request):
    return render(request,'project/index.html',{}) 