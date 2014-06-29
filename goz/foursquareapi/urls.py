from django.conf.urls import patterns, url
from .views import FsAuth, FsCallback

urlpatterns = patterns('',
  # Receive OAuth token from 4sq.
  url(r'^callback$', FsCallback.as_view(), name='oauth_return'),
  # Authenticate with 4sq using OAuth.
  url(r'^auth$', FsAuth.as_view(), name='oauth_auth'),
)
