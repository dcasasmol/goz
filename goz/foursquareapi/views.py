# foursquareapi/views.py

import json
from urllib.parse import urlencode
from urllib.request import urlopen, Request

from django.core.urlresolvers import reverse
from django.views.generic import RedirectView

from .config import CLIENT_ID, CLIENT_SECRET
from .config import request_token_url, access_token_url, redirect_url


class FsAuth(RedirectView):
  permanent = False

  def get_fs_auth_url(self):
    # Build the url to request.
    params = {'client_id': CLIENT_ID,
              'response_type': 'code',
              'redirect_uri': redirect_url}

    # Redirect the user to the url to confirm access for the app.
    return '%s?%s' % (request_token_url, urlencode(params))

  def get_redirect_url(self, *args, **kwargs):
    return self.get_fs_auth_url()


class FsCallback(RedirectView):
  permanent = False

  def set_access_token_in_session(self):
    # Get the code returned from foursquare.
    code = self.request.GET.get('code')

    # Build the url to request the access_token.
    params = {'client_id': CLIENT_ID,
              'client_secret': CLIENT_SECRET,
              'grant_type': 'authorization_code',
              'redirect_uri': redirect_url,
              'code': code}
    data = urlencode(params)
    req = Request('%s?%s' % (access_token_url, data))

    # Request the access_token.
    response = urlopen(req)
    access_token = json.loads(response.read().decode('utf-8'))
    access_token = access_token['access_token']

    # Store the access_token for later use.
    self.request.session['access_token'] = access_token

  def get_redirect_url(self, *args, **kwargs):
    self.set_access_token_in_session()

    # Redirect the user to show we're done.
    return reverse('home')


class FsUnauth(RedirectView):
  permanent = False

  def remove_session_data(self):
    del self.request.session['access_token']

  def get_redirect_url(self, *args, **kwargs):
    self.remove_session_data()

    # Redirect the user to show we're done.
    return reverse('index')


