from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import UpdateView

from .li_api import get_metadata_dict
from librarian import forms
from .models import Site


def editor_menu(request):
    sites = Site.objects.all()
    return render(request,'librarian/editor.html',{"sites":sites})

def site(request,site_id):
    return HttpResponse("hello world %s" % site_id)


class EditSiteView(UpdateView):
    model = Site
    form_class = forms.SiteForm
