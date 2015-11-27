from django.shortcuts import render
from django.http import HttpResponse

from .models import Site


def editor_menu(request):
    sites = Site.objects.filter()
    return render(request,'librarian/editor.html',{"sites":sites})

def site(request,site_id):
    return HttpResponse("hello world %s" % site_id)
