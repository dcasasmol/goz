# dbapi/exceptions.py:

from utils.exception import GeneralException


class UserNotSaved(GeneralException):
  def __init__(self):
    msg = 'User not saved'

    GeneralException.__init__(self, msg)
