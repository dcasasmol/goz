# utils/views.py

import string
import random

def generate_password(size=8, special_characters=False):
  '''Generates a valid password from the given lenght.

  If `special_characters` is True, the password could contain special
  characters. Otherwise, the password only could contain letters
  (uppercase and lowercase) and digits.

  Args:
    size (int): Password size, default 8.
    special_characters (bool): Contains special characters or not,
      default False.

  Returns:
    str: The password generated.

  '''
  allowed_characters = string.ascii_letters + string.digits

  if special_characters:
    allowed_characters = allowed_characters + string.punctuation

  return ''.join((random.choice(allowed_characters)) for x in range(size))


def is_valid_password(password, size=8, special_characters=False):
  '''Checks if the given password is valid or not.

  If `size` is given, compares `password` length against given `size` length.
  Otherwise, compares `password` length against 8 by default.

  If `special_characters` is True, special characters are allowed in password
  check. Otherwise, special characters are not allowed (only lowercase/uppercase
  letters and digits).

  Args:
    password (str): Password to check.
    size (int, optional): Password size to check, default 8.
    special_characters (bool, optional): Password can contain special characters
      or not, default False.

  Returns:
    bool: True if successful, False otherwise.

  '''
  allowed_characters = string.ascii_letters + string.digits

  if special_characters:
    allowed_characters = allowed_characters + string.punctuation

  is_valid = (len(password) == size)

  if is_valid:
    for one_letter in password:
      is_valid = is_valid and (one_letter in allowed_characters)

  return is_valid
