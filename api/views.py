from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def Index(request):
    return HttpResponse("<h1 align='center'>Hellow i'm Working too ....</h1>")


def MEMBER_DETAILS_REGISTER(request):
    pass