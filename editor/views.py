from django.shortcuts import render

from librarian.models import Site


def editor_menu(request):
    sites = Site.objects.filter()
    return render(request,'mapapp/editor.html',{})