from django.shortcuts import render

from django.http import HttpResponse

import time

def index(request):
    return HttpResponse("Hello, world. You're at the apps index.")

def wait_event(request):
    time.sleep(5)
    return HttpResponse("This page is displayed after 5 second wait.")

