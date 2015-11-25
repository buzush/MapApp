from django.conf.urls import url
from . import views

urlpatterns = [
                url(r'^$', views.editor_menu, name='editor'),
            ]
