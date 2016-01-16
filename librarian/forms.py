import floppyforms.__future__ as forms

from . import models


class SiteForm(forms.ModelForm):
    class Meta:
        model = models.Site
        exclude = (
        )


class ContentForm(forms.ModelForm):
    class Meta:
        model = models.Content
        exclude = (
        )
