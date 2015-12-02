from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.SiteListView.as_view(), name='list'),
    url(r'^add$', views.SiteCreateView.as_view(), name='add_site'),
    url(r'^(?P<pk>\d+)/$', views.SiteDetailView.as_view(), name='view_site'),
    url(r'^(?P<pk>\d+)/edit/$', views.SiteUpdateView.as_view(), name='update_site'),
    url(r'^(?P<site_pk>\d+)/add-content/$', views.ContentCreateView.as_view(), name='create_content'),
]
