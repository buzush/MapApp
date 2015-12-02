from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.utils.translation import ugettext_lazy as _

class Site(models.Model):
    name = models.CharField(_("name"), max_length=30, blank=False)
    additional_text = models.CharField(_('additional text'), max_length=30)
    location = models.PointField(_('location'), default=Point(x=37.36198, y=39.22079))
    radius = models.PositiveSmallIntegerField(_('radius'), default=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('site')
        verbose_name_plural =  _('sites')


class Content(models.Model):
    site = models.ForeignKey(Site, verbose_name="אתר מקושר")
    CONTENT_TYPES = (
        ("IMG", "תמונה"),
        ("SNG", "שיר"),
        ("MAP", "מפה"),
        ("TRV", "יומן מסע"),
        ("VID", "קטע וידאו"),
        ("OTR", "אחר"),
    )
    content_type = models.CharField("סוג התוכן", max_length=3, choices=CONTENT_TYPES)
    name = models.CharField("שם או כותרת", max_length=20)
    description = models.CharField("תיאור התוכן", max_length=200)
    link = models.URLField("קישור לתוכן")
    date = models.DateField("תאריך התוכן")

    def __str__(self):
        return "{}: {}".format(
            self.get_content_type_display(),
            self.name
        )

    class Meta:
        verbose_name = _("content")
        verbose_name_plural = "תכנים"
