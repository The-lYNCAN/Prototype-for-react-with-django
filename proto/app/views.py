from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.

def index(request):
    jsonres = {
        "username":"test",
        "value":"Hello world"
    }
    return JsonResponse(jsonres)