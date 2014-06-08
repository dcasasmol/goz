# foursquareapi/models.py

import json
import urllib
import datetime

from .exceptions import EndpointError

class FsApi:

  def __init__(self, access_token):
    self.base_url = 'https://api.foursquare.com/v2'
    self.datetime = datetime.datetime.now().strftime("%Y%m%d")
    self.access_token = access_token

  def __build_url(self, endpoint=None, params={}):
    if not endpoint:
      raise EndpointError

    encoded_params = urllib.parse.urlencode(params)

    return '%s/%s?%s' % (self.base_url, endpoint, encoded_params)

  def request(self, endpoint=None, params={}):
    try:
      params['oauth_token'] = self.access_token
      params['v'] = self.datetime

      url = self.__build_url(endpoint, params)

      request = urllib.request.urlopen(url)
      response = request.read()
      json_response = json.loads(response.decode(), encoding='utf8')

      return json_response

    except Exception as e:
      print(e.traceback())

  def get_user_info(self):
    return self.request('users/self')

