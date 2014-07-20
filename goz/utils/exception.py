# utils/exception.py

import traceback


class GeneralException(Exception):
  '''Base class to manage the custom exceptions that you need to raise.

  '''
  def __init__(self, msg):
    '''Creates the exception and set the `msg` attribute.

    Args:
      msg (str): Human readable string describing the exception.

    Attributes:
      msg (str): Human readable string describing the exception.

    '''
    self.msg = msg

  def __str__(self):
    '''Displays a human-readable representation of the Exception object.

    Returns:
      str: Human-readable representation of the Exception object.

    '''
    return self.msg

  @property
  def name(self):
    '''Gets the exception name.

    Returns:
      str: Exception name.

    '''
    return self.__class__.__name__

  @property
  def traceback(self):
    '''Gets the traceback of the last exception.

    Returns:
      str: Last exception traceback.

    '''
    try:
      lines = []

      lines.append('%s exception catched.' % self.name)
      lines.append(traceback.format_exc())
    except Exception as e:
      lines.append('%s exception can not be handled.' % self.name)
      lines.append(str(e))

    return '\n'.join(lines)
