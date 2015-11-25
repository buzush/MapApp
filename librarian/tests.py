from django.contrib.gis.geos import Point
from django.test import TestCase

from . import models


class LibrarianTests(TestCase):
    def test_create_site_and_content(self):
        site = models.Site.objects.create(
            name="Fistuk's House",
            additional_text="Full of surprises",
            location=Point(x=37.22, y=39.11),
            radius=40,
        )

        assert site.content_set.count() == 0

        site.content_set.create(
            content_type="IMG",
            name="The house from above",
            description="Wonderful picture, taken by Rega.",
            link="http://rega.com/123.gif",
            date="2010-10-02",
        )

        assert site.content_set.count() == 1
