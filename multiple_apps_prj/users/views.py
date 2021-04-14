from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("Placeholder for users to create a new user record.")

def login(request):
    return HttpResponse("Placeholder for users to log in.")

def user(request):
    return HttpResponse("Placeholder to later display all the lists of users.")
