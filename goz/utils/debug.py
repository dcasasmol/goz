# utils/debug.py


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
