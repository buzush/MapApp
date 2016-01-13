from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^map/$', views.map, name='map'),
    url(r'^sites/$', views.sites, name='sites'),
    url(r'^sites/(?P<pk>\d+)/modal/$', views.SiteModalView.as_view(), name='site_modal'),
]
