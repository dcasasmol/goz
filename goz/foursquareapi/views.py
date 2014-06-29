# foursquareapi/views.py

import json
import urllib

from django.core.urlresolvers import reverse
from django.views.generic import RedirectView

from .config import CLIENT_ID, CLIENT_SECRET
from .config import request_token_url, access_token_url, redirect_url


class FsAuth(RedirectView):
  permanent = False
  client_id = CLIENT_ID
  client_secret = CLIENT_SECRET

  def get_fs_auth_url(self):
    # Build the url to request.
    params = {'client_id': self.client_id,
              'response_type': 'code',
              'redirect_uri': redirect_url}

    # Redirects the user to the url to confirm access for the app.
    return '%s?%s' % (request_token_url, urllib.parse.urlencode(params))

  def get_redirect_url(self, *args, **kwargs):
    return self.get_fs_auth_url()


class FsCallback(RedirectView):
  permanent = False
  client_id = CLIENT_ID
  client_secret = CLIENT_SECRET

  def set_access_token_in_session(self):
    # Gets the code returned from foursquare.
    code = self.request.GET.get('code')

    # Builds the url to request the access_token.
    params = {'client_id': self.client_id,
              'client_secret': self.client_secret,
              'grant_type': 'authorization_code',
              'redirect_uri': redirect_url,
              'code': code}
    data = urllib.parse.urlencode(params)
    req = urllib.request.Request('%s?%s' % (access_token_url, data))

    # Gets the access_token.
    response = urllib.request.urlopen(req)
    access_token = json.loads(response.read().decode('utf-8'))
    access_token = access_token['access_token']

    # Stores the access_token for later use.
    self.request.session['access_token'] = access_token

  def get_redirect_url(self, *args, **kwargs):
    self.set_access_token_in_session()

    # Redirects the user to show we're done.
    return reverse('login')
