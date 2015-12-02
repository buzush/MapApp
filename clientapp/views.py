from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.utils.translation import ugettext_lazy as _
from librarian import models


def site(request, site_id):
    return HttpResponse("hello world %s" % site_id)


def client(request):
    return HttpResponse("client!")


def index(request):
    template = loader.get_template('clientapp/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


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
         } for site in qs]
    # print(qs.count())
    # d = serialize('geojson', qs, geometry_field='x', fields=(
    #     'name',
    # ))
    # assert False, d
    return JsonResponse({'points': l})
