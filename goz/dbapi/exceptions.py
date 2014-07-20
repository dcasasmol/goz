# dbapi/exceptions.py:

from utils.exception import GeneralException


class UserNotSaved(GeneralException):
  '''Exception raised when an User object exists but is not saved in database.

  If the User object is not saved in database, not have a Django User object
  in the `user` attribute.

  '''
  def __init__(self):
    '''Creates the exception and set the `msg` attribute.

    Attributes:
      msg (str): Human readable string describing the exception.

    '''
    msg = 'User not saved'

    GeneralException.__init__(self, msg)
