from django.conf.urls import patterns, include, url
from .views import login

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'goz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', login, name='login'),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^fsapi/', include(foursquareapi.urls)),
)
