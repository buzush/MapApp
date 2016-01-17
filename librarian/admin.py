from django.contrib.gis import admin

# from librarian.views import DEFAULT_CENTER
from . import models
from leaflet.admin import LeafletGeoAdmin


class ContentInline(admin.StackedInline):
    model = models.Content
    extra = 0


class SiteAdmin(LeafletGeoAdmin):
    inlines = [
        ContentInline,
    ]


admin.site.register(models.Content)
admin.site.register(models.Site, SiteAdmin)
admin.site.register(models.Collection)
