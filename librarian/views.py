from authtools.views import LoginRequiredMixin
from django import forms
from django.contrib.gis.geos import Point
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import UpdateView, DetailView, ListView, DeleteView
from django.views.generic.edit import CreateView
from leaflet.forms.widgets import LeafletWidget

from . import models

DEFAULT_CENTER = Point(x=35.093303, y=31.976406)


class SiteListView(LoginRequiredMixin, ListView):
    model = models.Site


class SiteDetailView(LoginRequiredMixin, DetailView):
    model = models.Site


class SiteForm(forms.ModelForm):
    class Meta:
        model = models.Site
        fields = ['name', 'additional_text', 'location', 'radius']
        widgets = {'location': LeafletWidget()}

class SiteMixin(LoginRequiredMixin):
    model = models.Site
    form_class=SiteForm


class SiteCreateView(SiteMixin, CreateView):
    def get_initial(self):
        d = super().get_initial()
        d['location'] = DEFAULT_CENTER
        return d



class SiteDeleteView(SiteMixin, DeleteView):
    success_url = '/lib/'
    pass


class SiteUpdateView(SiteMixin, UpdateView):
    pass


class ContentMixin(LoginRequiredMixin):
    model = models.Content
    fields = [
        'content_type',
        'name',
        'description',
        'link',
        'date',
    ]

    def dispatch(self, request, *args, **kwargs):
        self.site = get_object_or_404(models.Site, pk=self.kwargs['site_pk'])
        return super().dispatch(request, *args, **kwargs)


class ContentListView(LoginRequiredMixin, ListView):
    model = models.Content


class ContentDetailView(LoginRequiredMixin, DetailView):
    model = models.Content


class ContentCreateView(ContentMixin, CreateView):
    def form_valid(self, form):
        # THIS RUNS BEFORE SAVE
        form.instance.site = self.site
        return super().form_valid(form)


class ContentUpdateView(ContentMixin, UpdateView):
    pass


class ContentDeleteView(ContentMixin, DeleteView):
    def get_success_url(self):
        return reverse('content_list', kwargs={'site_pk': self.site.id})
