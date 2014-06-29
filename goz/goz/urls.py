# goz/urls.py

from django.contrib import admin
from django.conf.urls import patterns, include, url

from .views import Index, Login, Logout, Home


admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', Index.as_view(), name='index'),
  url(r'^i18n/', include('django.conf.urls.i18n')),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^fsapi/', include('foursquareapi.urls')),
  url(r'^home/?$', Home.as_view(), name='home'),
  url(r'^login/?$', Login.as_view(), name='login'),
  url(r'^logout/?$', Logout.as_view(), name='logout'),
)
