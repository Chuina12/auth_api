import json
from django import views
from django.http import JsonResponse
from django.shortcuts import redirect, render
import requests 
from rest_framework.decorators import api_view
@api_view(['POST'])
def asyncCreateUser(request):
    if request.method == "POST":
        data = request.data
        kmail_user = requests.post('http://kmail.africa/signup', json=data)
        klapeers_user = requests.post('http://klapeers.com/signup', json=data)
        
        if kmail_user.status_code == 200 and  klapeers_user.status_code == 200:
            return JsonResponse({"status":200, "result": "success", "msg": "Compte cree avec success"})
        else:
            return JsonResponse({"kmail_error": kmail_user.json(), "klapeers_error": klapeers_user.json()})
      
def conpte(request):
    return render(request, 'compte.html')