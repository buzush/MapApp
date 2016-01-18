import floppyforms.__future__ as forms
from django.utils.translation import ugettext_lazy as _
from leaflet.forms.widgets import LeafletWidget

from librarian import primo
from . import models


class SiteForm(forms.ModelForm):
    class Meta:
        model = models.Site
        fields = [
            'name',
            'additional_text',
            'location',
            'radius',
        ]
        widgets = {'location': LeafletWidget()}


class PrimoURLField(forms.URLField):
    def clean(self, value):
        url = super().clean(value)
        try:
            doc_id = primo.extract_doc_id(url)
        except KeyError:
            raise forms.ValidationError(_("Primo doc id not found in url"))
        return doc_id

class FromUrlForm(forms.Form):
    doc_id = PrimoURLField(label=_("Resource URL"))
