# foursquareapi/models.py

import json
import urllib
import logging
import datetime

from .config import FS_API_BASE_URL
from .exceptions import EndpointError
from goz.settings import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class FsApi:
  '''This class models a client to make request to the *Foursquare* API.

  '''
  def __init__(self, access_token):
    '''Create the `FsApi` object and set the attributes.

    Args:
      access_token (str): *Foursquare* api access token.

    Attributes:
      base_url (str): *Foursquare* api base url.
      datetime (str): Today date.
      access_token (str): *Foursquare* api access token.

    '''
    self.base_url = FS_API_BASE_URL
    self.datetime = datetime.datetime.now().strftime("%Y%m%d")
    self.access_token = access_token

  def _build_url(self, endpoint=None, params={}):
    '''Builds a url to make a request to the *Foursquare* API.

    Args:
      endpoint (str): API endpoint, default None.
      params (dict): Params to encode in the API request.

    Returns:
      str: Url of the *Foursquare* API to make a request.

    Raises:
      EndpointError: If `endpoint` is None.

    '''
    if not endpoint:
      raise EndpointError

    encoded_params = urllib.parse.urlencode(params)

    return '%s/%s?%s' % (self.base_url, endpoint, encoded_params)

  def request(self, endpoint=None, params={}):
    '''Makes a request to the *Foursquare* API.

    Args:
      endpoint (str): API endpoint, default None.
      params (dict): Params to encode in the API request.

    Returns:
      dict: JSON response of the *Foursquare* API.

    '''
    try:

      params['oauth_token'] = self.access_token
      params['v'] = self.datetime

      url = self._build_url(endpoint, params)

      request = urllib.request.urlopen(url)
      response = request.read()
      json_response = json.loads(response.decode(), encoding='utf8')

      return json_response

    except Exception as e:

      raise e

  def get_user_info(self):
    '''Gets the user info from *Foursquare* API.

    Returns:
      dict: User info with using this format::
        {
          'meta': Request info,
          'response': User info
        }

    '''
    response = self.request('users/self')

    user_info = {}
    user_info['meta'] = response.get('meta', {})
    user_info['response'] = {}

    fs_response_info = response.get('response', {})
    if fs_response_info:
      fs_user_info = fs_response_info.get('user', {})
      info = {
        'username': fs_user_info.get('id', ''),
        'first_name': fs_user_info.get('firstName', ''),
        'last_name': fs_user_info.get('lastName', ''),
        'gender': fs_user_info.get('gender', ''),
        'photo': fs_user_info.get('photo', {}).get('suffix', ''),
        'city': fs_user_info.get('homeCity', ''),
        'bio': fs_user_info.get('bio', ''),
        'email': fs_user_info.get('contact', {}).get('email', ''),
        'twitter': fs_user_info.get('contact', {}).get('twitter', ''),
        'facebook': fs_user_info.get('contact', {}).get('facebook', ''),
      }

      user_info['response'] = info

    return user_info
