# foursquareapi/exceptions.py

from utils.exception import GeneralException


class EndpointError(GeneralException):
  '''Exception raised when an endpoint is not given.

  If the endpoing is not given, the API url can not be built.

  '''
  def __init__(self):
    '''Creates the exception and set the `msg` attribute.

    Attributes:
      msg (str): Human readable string describing the exception.

    '''
    msg = 'Empty endpoint'

    GeneralException.__init__(self, msg)
