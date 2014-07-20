# foursquareapi/views.py

import json
import urllib

from django.core.urlresolvers import reverse
from django.views.generic import RedirectView

from .config import CLIENT_ID, CLIENT_SECRET
from .config import FS_AUTH_URL, FS_ACCESS_TOKEN_URL, GOZ_CALLBACK_URL


class FsAuth(RedirectView):
  '''This class models a request to the *Foursquare* authentication system.

  Attributes:
    permanent (bool): If the redirect is permanent, default False.
    client_id (str): *Foursquare* client id.
    client_secret (str): *Foursquare* client secret.

  '''
  permanent = False
  client_id = CLIENT_ID
  client_secret = CLIENT_SECRET

  def get_fs_auth_url(self):
    '''Gets the url to make the auth request.

    Returns:
      str: Url of the auth request.

    '''
    # Build the url to request.
    params = {'client_id': self.client_id,
              'response_type': 'code',
              'redirect_uri': GOZ_CALLBACK_URL}

    # Redirects the user to the url to confirm access for the app.
    return '%s?%s' % (FS_AUTH_URL, urllib.parse.urlencode(params))

  def get_redirect_url(self, *args, **kwargs):
    '''Override `get_redirect_url` method of `RedirectView` class.

    Args:
      *args: Variable length argument list.
      **kwargs: Arbitrary keyword arguments.

    Returns:
      str: Url of the auth request.

    '''
    return self.get_fs_auth_url()


class FsCallback(RedirectView):
  '''This class models a callback request from the *Foursquare* authentication
  system.

  Attributes:
    permanent (bool): If the redirect is permanent, default False.
    client_id (str): *Foursquare* client id.
    client_secret (str): *Foursquare* client secret.

  '''
  permanent = False
  client_id = CLIENT_ID
  client_secret = CLIENT_SECRET

  def set_access_token_in_session(self):
    '''Stores the access token in session.

    Make the request to get the access token and store it in session.

    '''
    # Gets the code returned from foursquare.
    code = self.request.GET.get('code')

    # Builds the url to request the access_token.
    params = {'client_id': self.client_id,
              'client_secret': self.client_secret,
              'grant_type': 'authorization_code',
              'redirect_uri': GOZ_CALLBACK_URL,
              'code': code}
    data = urllib.parse.urlencode(params)
    req = urllib.request.Request('%s?%s' % (FS_ACCESS_TOKEN_URL, data))

    # Gets the access_token.
    response = urllib.request.urlopen(req)
    js_access_token = json.loads(response.read().decode('utf-8'))
    access_token = js_access_token['access_token']

    # Stores the access_token for later use.
    if not 'login' in self.request.session:
      self.request.session['login'] = {}

    self.request.session['login']['access_token'] = access_token

  def get_redirect_url(self, *args, **kwargs):
    '''Override `get_redirect_url` method of `RedirectView` class.

    Stores the access token in session.

    Args:
      *args: Variable length argument list.
      **kwargs: Arbitrary keyword arguments.

    Returns:
      str: Login page url.

    '''
    self.set_access_token_in_session()

    # Redirects the user to show we're done.
    return reverse('login')
