from django.contrib.gis import admin
from .models import Site, Content


class ContentInline(admin.StackedInline):
    model = Content
    extra = 0

class SiteAdmin(admin.OSMGeoAdmin):
    inlines = [
        ContentInline,
    ]


admin.site.register(Content)
admin.site.register(Site, SiteAdmin)
