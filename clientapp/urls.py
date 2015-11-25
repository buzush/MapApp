from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^(?P<site_id>[0-9]+)/$', views.site),
]