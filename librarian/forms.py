import floppyforms.__future__ as forms
# from django import forms

from . import models


class SiteForm(forms.ModelForm):
    class Meta:
        model = models.Site
        exclude = (
        )
