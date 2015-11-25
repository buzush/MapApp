from django.shortcuts import render
from django.http import HttpResponse


def site(request,site_id):
    return HttpResponse("hello world %s" % site_id)
