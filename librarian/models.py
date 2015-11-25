from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Site(models.Model):
    site_id = models.AutoField(primary_key=True, verbose_name="מספר אתר")
    site_name = models.CharField(max_length=30, blank=False, verbose_name="שם אתר")
    additional_text = models.CharField(max_length=30, verbose_name="טקסט נוסף")
    location = models.PointField(default=Point(x=3736198,y=3922079))
    radius = models.PositiveSmallIntegerField(default="200", verbose_name="רדיוס")

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = "אתר"
        verbose_name_plural= "אתרים"

class Content(models.Model):
    site = models.ForeignKey(Site, verbose_name="אתר מקושר",blank=False)
    content_id = models.AutoField(primary_key=True)
    CONTENT_TYPES =(
        ("IMG", "תמונה"),
        ("SNG", "שיר"),
        ("MAP", "מפה"),
        ("TRV", "יומן מסע"),
        ("VID", "קטע וידאו"),
        ("OTR", "אחר"),
    )
    content_type = models.CharField(max_length=3,choices=CONTENT_TYPES,blank=False,verbose_name="סוג התוכן")
    name = models.CharField(verbose_name="שם או כותרת",max_length=20)
    description = models.CharField(verbose_name="תיאור התוכן",max_length=200)
    link = models.URLField(verbose_name="קישור לתוכן",blank=False)
    date = models.DateField(verbose_name="תאריך התוכן")

    def __str__(self):
        return self.content_type+":"+self.name

    class Meta:
        verbose_name = "תוכן"
        verbose_name_plural = "תכנים"