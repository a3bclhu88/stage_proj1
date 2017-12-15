from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

#function based view example

def home(request):
  num = random.randint(0,100)
  return render(request,"base.html",{"html_var":"request content unknown","random_num":num})
