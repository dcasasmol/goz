from django.conf.urls import patterns, url
from .views import FsAuth, FsCallback, FsUnauth

urlpatterns = patterns('',
  # Receive OAuth token from 4sq.
  url(r'^callback$', FsCallback.as_view(), name='oauth_return'),
  # Logout from the app.
  url(r'^logout$', FsUnauth.as_view(), name='oauth_unauth'),
  # Authenticate with 4sq using OAuth.
  url(r'^auth$', FsAuth.as_view(), name='oauth_auth'),
)
