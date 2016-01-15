from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class Site(models.Model):
    name = models.CharField(_("name"), max_length=30, blank=False)
    additional_text = models.CharField(_('additional text'), max_length=30)
    location = models.PointField(_('location'))
    radius = models.PositiveSmallIntegerField(_('radius'), default=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("view_site", args=(self.pk,))

    def get_modal_url(self):
        return reverse("site_modal", args=(self.pk,))

    def get_edit_url(self):
        return reverse("update_site", args=(self.pk,))

    class Meta:
        verbose_name = _('site')
        verbose_name_plural = _('sites')


class Content(models.Model):
    site = models.ForeignKey(Site, verbose_name="אתר מקושר",
                             related_name="contents")

    class Type:
        IMG = "IMG"
        SNG = "SNG"
        MAP = "MAP"
        TRV = "TRV"
        OTR = "OTR"

        choices = (
            (IMG, "תמונה"),
            ("SNG", "שיר"),
            ("MAP", "מפה"),
            ("TRV", "יומן מסע"),
            ("VID", "קטע וידאו"),
            ("OTR", "אחר"),
        )

    content_type = models.CharField("סוג התוכן", max_length=3,
                                    choices=Type.choices)
    name = models.CharField("שם או כותרת", max_length=20)
    description = models.CharField("תיאור התוכן", max_length=200)
    link = models.URLField("קישור לתוכן")
    date = models.DateField("תאריך התוכן")

    def __str__(self):
        return "{}: {}".format(
                self.get_content_type_display(),
                self.name
        )

    def get_template_name(self):
        return "clientapp/content/_{}.html".format(self.content_type.lower())

    def get_absolute_url(self):
        return reverse("view_content", args=(self.site.id, self.pk))

    def get_edit_url(self):
        return reverse("update_content", args=(self.site.id, self.pk))

    class Meta:
        verbose_name = _("content")
        verbose_name_plural = "תכנים"

    def get_model_fields(self):
        result = []
        for field_instance in self._meta.get_fields():
            result.append(
                    (field_instance.name, getattr(self, field_instance.name)))

        return result
