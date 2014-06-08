# utils/exception.py

import traceback


class GeneralException(Exception):
  def __init__(self, msg):
    self.msg = msg

  def __str__(self):
    return '[ERROR] %s' % self.msg

  def get_name(self):
    '''
      Gets the exception name
    '''
    return self.__class__.__name__

  def traceback(self):
    '''
      Prints the traceback of the last exception
    '''
    try:
      print(traceback.format_exc())
    except Exception as e:
      print('[ERROR] %s can not be handled.' % self.get_name())
      print('[DEBUG] %s' % str(e))
