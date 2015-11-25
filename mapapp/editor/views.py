from django.shortcuts import render
from django.http import HttpResponse

def editor_menu(request):
    return render(request,'mapapp/editor.html',{})