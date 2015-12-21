from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.utils.translation import ugettext_lazy as _
from librarian.models import Site


class Client(models.Model):
    location = models.PointField(_('location'))
    radius = models.PositiveSmallIntegerField(_('radius'), default=200)
    site = Site()

    def __str__(self):
        return self.site.name
