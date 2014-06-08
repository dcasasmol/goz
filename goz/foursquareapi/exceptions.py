# foursquareapi/exceptions.py

from utils.exception import GeneralException


class EndpointError(GeneralException):
  def __init__(self):
    msg = 'Empty endpoint'

    GeneralException.__init__(self, msg)
