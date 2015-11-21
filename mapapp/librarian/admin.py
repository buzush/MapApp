from django.contrib.gis import admin
from .models import Site, Content

admin.site.register(Site, admin.OSMGeoAdmin)

admin.site.register(Content)
