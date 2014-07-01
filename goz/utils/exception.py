# utils/exception.py

import traceback


class GeneralException(Exception):
  def __init__(self, msg):
    self.msg = msg

  def __str__(self):
    return self.msg

  @property
  def name(self):
    '''
      Gets the exception name
    '''
    return self.__class__.__name__

  @property
  def traceback(self):
    '''
      Gets the traceback of the last exception
    '''
    try:
      lines = []

      lines.append('%s exception catched.' % self.name)
      lines.append(traceback.format_exc())
    except Exception as e:
      lines.append('%s exception can not be handled.' % self.name)
      lines.append(str(e))

    return '\n'.join(lines)
