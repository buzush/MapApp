import json

from authtools.views import LoginRequiredMixin
from django.contrib.gis.geos import Point
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import UpdateView, DetailView, ListView, DeleteView, \
    FormView
from django.views.generic.edit import CreateView

from librarian import nli
from librarian import primo
from . import forms
from . import models


class SiteListView(LoginRequiredMixin, ListView):
    model = models.Site

    def get_context_data(self, *args, **kwargs):
        context = super(SiteListView, self).get_context_data(*args, **kwargs)
        context['settings_dict'] = {}
        context['settings_dict']['RESET_VIEW'] = False
        return context


class SiteDetailView(LoginRequiredMixin, DetailView):
    model = models.Site

    def get_context_data(self, *args, **kwargs):
        context = super(SiteDetailView, self).get_context_data(*args, **kwargs)
        context['settings_dict'] = {}
        context['settings_dict']['RESET_VIEW'] = False
        return context


class SiteMixin(LoginRequiredMixin):
    model = models.Site
    form_class = forms.SiteForm


class SiteCreateView(SiteMixin, CreateView):
    def get_initial(self):
        DEFAULT_CENTER = Point(x=35.093303, y=31.976406)
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
        'collection',
        'content_type',
        'name',
        'creator',
        'creator_2',
        'performing',
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


class ContentCreateFromURLView(ContentMixin, FormView):
    template_name = "librarian/content_from_url.html"
    form_class = forms.FromUrlForm

    def form_valid(self, form):
        return redirect("create_content", self.site.id,
                        form.cleaned_data['doc_id'])


class ContentCreateView(ContentMixin, CreateView):
    def form_valid(self, form):
        form.instance.site = self.site
        form.instance.doc_id = form.initial['doc_id']
        form.instance.full_record = json.dumps(self.record, indent=2)
        return super().form_valid(form)

    def get_initial(self):
        d = super().get_initial()
        doc_id = self.kwargs['doc_id']
        self.record = primo.primo_request(doc_id)
        data = nli.parse_record(self.record)
        collection, created = models.Collection.objects.get_or_create(
                code=data['collection_code'],
                defaults={
                    'title': data['collection_title'],
                })
        data['collection'] = collection.id
        d.update(data)
        return d

    def get_success_url(self):
        return self.site.get_absolute_url()


class ContentUpdateView(ContentMixin, UpdateView):
    pass


class ContentDeleteView(ContentMixin, DeleteView):
    def get_success_url(self):
        return reverse('content_list', kwargs={'site_pk': self.site.id})
