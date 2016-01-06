from django.contrib.gis import admin

#from librarian.views import DEFAULT_CENTER
from .models import Site, Content
from leaflet.admin import LeafletGeoAdmin


class ContentInline(admin.StackedInline):
    model = Content
    extra = 0


class SiteAdmin(LeafletGeoAdmin):
    inlines = [
        ContentInline,
    ]


admin.site.register(Content)
admin.site.register(Site, SiteAdmin)
