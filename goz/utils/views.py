# utils/views.py

import string
import random

def generate_password(size=8, special_characters=False):
  chars = string.ascii_letters + string.digits

  if special_characters:
    chars = chars + string.punctuation

  return ''.join((random.choice(chars)) for x in range(size))

