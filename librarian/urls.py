from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.editor_menu, name='list'),
    url(r'^add$', views.AddSite.as_view(), name='add_site'),
    url(r'^(?P<pk>\d+)/$', views.SiteDetailView.as_view(), name='view_site'),
]
