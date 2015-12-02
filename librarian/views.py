from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import UpdateView, DetailView
from django.views.generic.edit import CreateView, FormView

from .li_api import get_metadata_dict
from librarian import forms
from .models import Site


def editor_menu(request):
    sites = Site.objects.all()
    return render(request, 'librarian/site_list.html', {"sites": sites})


class AddSite(CreateView):
    model = Site
    fields = ['name', 'additional_text', 'location', 'radius']


class SiteDetailView(DetailView):
    model = Site


def site(request, site_id):
    return HttpResponse("hello world %s" % site_id)


class EditSiteView(UpdateView):
    model = Site
    form_class = forms.SiteForm
