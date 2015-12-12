from django.shortcuts import get_object_or_404

from django.views.generic import UpdateView, DetailView, ListView, DeleteView
from django.views.generic.edit import CreateView

from . import models


class SiteListView(ListView):
    model = models.Site


class SiteDetailView(DetailView):
    model = models.Site


class SiteMixin:
    model = models.Site
    fields = ['name', 'additional_text', 'location', 'radius']


class SiteCreateView(SiteMixin, CreateView):
    pass

class SiteDeleteView(SiteMixin, DeleteView):
    success_url = '/lib/'
    pass


class SiteUpdateView(SiteMixin, UpdateView):
    pass


class ContentMixin:
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


class ContentListView(ListView):
    model = models.Content


class ContentDetailView(DetailView):
    model = models.Content


class ContentCreateView(ContentMixin, CreateView):
    def form_valid(self, form):
        # THIS RUNS BEFORE SAVE
        form.instance.site = self.site
        return super().form_valid(form)


class ContentUpdateView(ContentMixin, UpdateView):
    pass
