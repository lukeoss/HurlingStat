from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
import json

def hello(request):
    return HttpResponse("Hello, World!")

def test_api(request):
    return JsonResponse({"message": "Hello from Django!"})


@csrf_exempt
@require_http_methods(["POST"])
def create_account(request):
    try:
        data = json.loads(request.body)
        user = User.objects.create_user(
            username=data['email'], 
            email=data['email'], 
            password= make_password(data['password'])
        )
        return JsonResponse({"message": "User created successfully."}, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
