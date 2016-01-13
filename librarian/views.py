from authtools.views import LoginRequiredMixin
from django import forms
from django.contrib.gis.geos import Point
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import UpdateView, DetailView, ListView, DeleteView, \
    FormView
from django.views.generic.edit import CreateView
from leaflet.forms.widgets import LeafletWidget

from librarian.importer import get_primo_data
from . import models


class SiteListView(LoginRequiredMixin, ListView):
    model = models.Site
    def get_context_data(self, *args,**kwargs):
        context = super(SiteListView,self).get_context_data(*args,**kwargs)
        context['settings_dict']={}
        context['settings_dict']['RESET_VIEW']= False
        return context


class SiteDetailView(LoginRequiredMixin, DetailView):
    model = models.Site
    def get_context_data(self, *args,**kwargs):
        context = super(SiteDetailView,self).get_context_data(*args,**kwargs)
        context['settings_dict']={}
        context['settings_dict']['RESET_VIEW']= False
        return context



class SiteForm(forms.ModelForm):
    class Meta:
        model = models.Site
        fields = ['name', 'additional_text', 'location', 'radius']
        widgets = {'location': LeafletWidget()}


class SiteMixin(LoginRequiredMixin):
    model = models.Site
    form_class = SiteForm


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


class FromUrlForm(forms.Form):
    url = forms.URLField()  # TODO: validate is primo URL using validators=[PrimoURLValidator()]


class ContentCreateFromURLView(ContentMixin, FormView):
    template_name = "librarian/content_from_url.html"
    form_class = FromUrlForm


class ContentCreateView(ContentMixin, CreateView):
    def form_valid(self, form):
        # THIS RUNS BEFORE SAVE
        form.instance.site = self.site
        return super().form_valid(form)

    def get_initial(self):
        d = super().get_initial()
        if 'url' in self.request.GET:
            # TODO: doc_id = extract_doc_id(self.request.GET['url'])
            doc_id = "NNL_ALEPH003440887"
            data = get_primo_data(doc_id)
            d['name'] = data['name']
            # or: d.update(data)
        return d


class ContentUpdateView(ContentMixin, UpdateView):
    pass


class ContentDeleteView(ContentMixin, DeleteView):
    def get_success_url(self):
        return reverse('content_list', kwargs={'site_pk': self.site.id})
