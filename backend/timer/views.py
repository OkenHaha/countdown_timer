from django.shortcuts import render, redirect
from django.contrib import messages
 
## import todo form and models

 
###############################################
 
def index(request):
    return render(request, 'timer/index.html')
