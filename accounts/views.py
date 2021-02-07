import json

from django.shortcuts import render
from django.contrib.auth.models import auth
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view

from accounts.models import BakeryUser

# Create your views here.
@csrf_exempt 
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is None:
            return HttpResponse(json.dumps({'result':False, 'message': 'Invalid credentials'}))
        else:
            return HttpResponse(json.dumps({'result':True, 'message': 'Login successful'}))
    else:
        return HttpResponse('Only POST is supported in login method')

@csrf_exempt
def logout(request):
    try:
        auth.logout(request)
    except:
        pass
    return HttpResponse(json.dumps({'result':True, 'message': 'Logout successful'}))

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        roles = 'customer'

        if BakeryUser.objects.filter(username=username).exists():
            return HttpResponse(json.dumps({'result': False, 'message': 'This username is already taken'})) 

        if BakeryUser.objects.filter(email=email).exists():
            return HttpResponse(json.dumps({'result': False, 'message': 'An account with this email already exists'}))

        buser = BakeryUser(first_name=first_name, last_name=last_name, username=username, email=email,roles=roles)
        buser.set_password(password)
        buser.save()
        return HttpResponse(json.dumps({'result': True, 'message': f'User {username} created successfully.'}))
    else:
        return HttpResponse('Only POST is supported in register method')

         