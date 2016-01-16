from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView

from librarian import models


def mapi(request):
    template = loader.get_template('clientapp/map.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def map(request):
    return render(request, 'clientapp/map.html', {})


def sites(request):
    qs = models.Site.objects.all()
    l = [{
             'name': site.name,
             'lat': site.location.x,
             'lng': site.location.y,
             'modal_url': site.get_modal_url(),
         } for site in qs]
    return JsonResponse({'points': l})


class SiteModalView(DetailView):
    model = models.Site
    template_name = "clientapp/site_modal.html"
