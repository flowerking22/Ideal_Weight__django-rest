from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.http import Http404
from django.core import serializers
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
@api_view(['POST'])
def IdealWeight(request):
    try:
        height=json.loads(request.body)
        weight=str(height*10)
        return JsonResponse("Ideal Weight Should be:"+weight+" kg",safe=False)
    except ValueError as e:
        return JsonResponse("Welcome",safe=False)