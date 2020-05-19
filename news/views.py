from django.shortcuts import render
from django.http import HttpResponse

#our views functions
def welcome(request):
    return HttpResponse('Welcome to The Moringa Tribune')
