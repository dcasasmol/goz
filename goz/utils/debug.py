# utils/debug.py

from traceback import format_exc

def debug(obj, label='DEBUG'):
  '''
    Prints the given item

    :param item: Variable's name
    :type item: Str
  '''
  try:
    print('[%s]: %s' % (label, obj))
  except Exception as e:
    print('[DEBUG]: Object can not be printed. %s' % str(e))


def handle_exception():
  '''
    Prints the traceback of the last exception
  '''
  try:
    print(format_exc())
  except Exception as e:
    print('[DEBUG]: Exception can not be handled. %s' % str(e))
